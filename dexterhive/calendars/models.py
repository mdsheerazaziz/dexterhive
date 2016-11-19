from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields.jsonb import JSONField


class CalendarEvents(models.Model):
    user = models.ForeignKey(User)
    event_id = models.CharField(max_length=127)
    summary = models.CharField(max_length=511, null=True)
    description = models.TextField(null=True)
    event_created_at = models.DateTimeField(null=True)
    event_updated_at = models.DateTimeField(null=True)
    event_start_at = models.DateTimeField(null=True)
    event_end_at = models.DateTimeField(null=True)
    event_link = models.CharField(max_length=511, null=True)
    organizer_name = models.CharField(max_length=127, null=True)
    organizer_email = models.CharField(max_length=511, null=True)
    creator_name = models.CharField(max_length=127, null=True)
    creator_email = models.CharField(max_length=511, null=True)
    attendees = JSONField(null=True)
    location = models.CharField(max_length=511, null=True)
    other_details = JSONField(null=True)
