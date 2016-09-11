from dexterhive.core.models import UserProfile


def get_user_details(user):
    user_profile = UserProfile.objects.get(user=user)
    return {'user_profile': user_profile.avatar}
