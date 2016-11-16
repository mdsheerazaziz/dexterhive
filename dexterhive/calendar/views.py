from dexterhive.calendar.resources import save_user_credentials
from django.http.response import HttpResponseRedirect, HttpResponse
from dexterhive.calendar.settings import GOOGLE_CALENDAR_OAUTH2_FLOW


def get_authorization_url(request):
    """
    """
    return HttpResponseRedirect(GOOGLE_CALENDAR_OAUTH2_FLOW.step1_get_authorize_url())


def save_credentials(request):
    authorization_code = request.GET.get('code', None)
    user = request.user
    save_user_credentials(user, authorization_code)
    # TODO Fix this once ui is ready
    return HttpResponse(status=200)

