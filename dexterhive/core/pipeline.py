from django.core.exceptions import ObjectDoesNotExist
from dexterhive.core import models


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
