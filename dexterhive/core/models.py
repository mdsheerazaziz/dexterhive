from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields.jsonb import JSONField


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


class UserAccessTokens(models.Model):
    """
        Stores the credentials details (Tokens) for user's different widgets
    """
    user = models.ForeignKey(User)
    widget_type = models.CharField(max_length=63)
    credential_details = JSONField()


class ThirdPartyIntegrations(models.Model):
    name = models.CharField(max_length=63)
    other_details = JSONField(null=True)


class UserThirdPartyIntegrationMapping(models.Model):
    user = models.ForeignKey(User)
    integration = models.ForeignKey(ThirdPartyIntegrations)
    integration_user_id = models.CharField(max_length=511)
    integration_password = models.CharField(max_length=31, null=True)


class Invitees(ModelBase):
    pass
