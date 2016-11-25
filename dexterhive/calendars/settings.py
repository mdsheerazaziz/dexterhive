from oauth2client.client import OAuth2WebServerFlow
from dexterhive.calendars.constants import GOOGLE_CALENDAR_PROMPT, GOOGLE_CALENDAR_REDIRECT_URI, \
    GOOGLE_CALENDAR_ACCESS_TYPE, GOOGLE_CALENDAR_CLIENT_ID, GOOGLE_CALENDAR_CLIENT_SECRET, GOOGLE_CALENDAR_SCOPE


GOOGLE_CALENDAR_OAUTH2_FLOW = OAuth2WebServerFlow(
    GOOGLE_CALENDAR_CLIENT_ID,
    GOOGLE_CALENDAR_CLIENT_SECRET,
    GOOGLE_CALENDAR_SCOPE,
    GOOGLE_CALENDAR_REDIRECT_URI,
    acess_type=GOOGLE_CALENDAR_ACCESS_TYPE,
    prompt=GOOGLE_CALENDAR_PROMPT)