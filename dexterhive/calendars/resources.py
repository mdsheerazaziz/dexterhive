import httplib2
from apiclient import discovery
from dexterhive.calendars.constants import GOOGLE_CALENDAR_SERVICE_NAME, GOOGLE_CALENDAR_SERVICE_VERSION3, \
    GOOGLE_CALENDAR_ID, GOOGLE_CALENDAR_ACCESS_TOKEN_WIDGET_NAME
from dexterhive.calendars.utils import format_timestamp
from oauth2client.client import Credentials
from dexterhive.calendars.settings import GOOGLE_CALENDAR_OAUTH2_FLOW
from dexterhive.core.models import UserAccessTokens
from dexterhive.calendars.models import CalendarEvents


def _fetch_credentials(code):
    credentials = GOOGLE_CALENDAR_OAUTH2_FLOW.step2_exchange(code)
    return credentials


def _get_user_credentials(user):
    credentials = UserAccessTokens.objects.filter(user=user, widget_type=GOOGLE_CALENDAR_ACCESS_TOKEN_WIDGET_NAME)
    return map((lambda credential: Credentials.new_from_json(credential.credential_details)), credentials)


def _authorize_credentials(credentials):
    return credentials.authorize(httplib2.Http())


def _build_google_service(service_name, service_version, http):
    return discovery.build(service_name, service_version, http=http)


def _create_event_objects(user, event):
    return CalendarEvents(user=user, event_id=event.get('id'), summary=event.get('summary'),
                          description=event.get('description'),
                          event_created_at=format_timestamp(event.get('created')),
                          event_updated_at=format_timestamp(event.get('updated')),
                          event_start_at=format_timestamp(event.get('start', {}).get('dateTime')),
                          event_end_at=format_timestamp(event.get('end', {}).get('dateTime')),
                          event_link=event.get('htmlLink'),
                          organizer_name=event.get('organizer', {}).get('displayName'),
                          organizer_email=event.get('organizer', {}).get('email'),
                          creator_name=event.get('creator', {}).get('displayName'),
                          creator_email=event.get('creator', {}).get('email'),
                          attendees=event.get('attendees'),
                          location=event.get('location'),
                          other_details=event)


def _save_calendar_event(user, raw_event_json):
    # TODO FIX THE REPEATED ENTRY (IT SHOULD NOT BE SAVED)
    events = raw_event_json.get('items')
    events_obj = []
    for event in events:
        events_obj.append(_create_event_objects(user, event))
    CalendarEvents.objects.bulk_create(events_obj)


def save_user_credentials(user, authorization_code):
    credentials = _fetch_credentials(authorization_code)
    UserAccessTokens(user=user, widget_type=GOOGLE_CALENDAR_ACCESS_TOKEN_WIDGET_NAME,
                     credential_details=credentials.to_json()).save()


def sync_user_google_calendar(user):
    credentials = _get_user_credentials(user)
    for credential in credentials:
        http = _authorize_credentials(credential)
        service = _build_google_service(GOOGLE_CALENDAR_SERVICE_NAME, GOOGLE_CALENDAR_SERVICE_VERSION3, http=http)
        # TODO CHECK AND FIX TO FETCH ALL EVENTS IF NOT FETCHING
        events_result = service.events().list(calendarId=GOOGLE_CALENDAR_ID).execute()
        print events_result
        _save_calendar_event(user, events_result)
