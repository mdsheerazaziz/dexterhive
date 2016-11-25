import requests
import uuid
from urlparse import urlparse, parse_qs
from dexterhive.core.constants import latex_register_url, latex_password_reset_url
from django.core.exceptions import ObjectDoesNotExist
from dexterhive.core import models
from dexterhive.settings import latex_url, is_latex_enabled


def get_avatar(backend, response, user=None, *args, **kwargs):
    """
        Gets the user avatar
    Args:
        backend: object from which user signup
        response: python social oauth response
        user: username
        *args: args list
        **kwargs: kwargs list
    """
    url = None
    if backend.name == 'google-oauth2':
        url = response.get('image', {}).get('url')
    if url:
        try:
            user_profile = models.UserProfile.objects.get(user=user)
            user_profile.avatar = url
            user_profile.save()
        except ObjectDoesNotExist:
            models.UserProfile(user=user, avatar=url).save()


def configure_latex(backend, response, user=None, *args, **kwargs):
    """
        Creates an account in sharelatex
    Args:
        backend: object from which user signup
        response: python social oauth response
        user: username
        *args: args list
        **kwargs: kwargs list
    """
    if is_latex_enabled:
        latex = models.ThirdPartyIntegrations.objects.get(name="sharelatex")

        if not models.UserThirdPartyIntegrationMapping.objects.filter(user=user, integration=latex).exists():
            latex_register_data = {'email': user.email}
            token_url = requests.post('{0}/{1}'.format(latex_url, latex_register_url),
                                      data=latex_register_data)

            token = parse_qs(urlparse(token_url.json()['setNewPasswordUrl']).query)['passwordResetToken'][0]
            integration_user_id = token_url.json()['id']
            password = str(uuid.uuid4().get_hex()[0:16])

            latex_password_reset_data = {'passwordResetToken': token, 'password': password}
            requests.post('{0}/{1}'.format(latex_url, latex_password_reset_url),
                          data=latex_password_reset_data)

            models.UserThirdPartyIntegrationMapping(user=user, integration=latex,
                                                    integration_user_id=integration_user_id,
                                                    integration_password=password).save()
