from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ModelBase(models.Model):
    """
        Store base attributes
    """
    created_at = models.DateTimeField(default=timezone.now)
    last_updated_at = models.DateTimeField(auto_now=True)


class UserProfile(ModelBase):
    """
        Store the user profile related information
    """
    user = models.OneToOneField(User)
    avatar = models.URLField(null=True)


class Invites(ModelBase):
    pass


