from __future__ import unicode_literals

from django.db import models
from dexterhive.groups.models import Groups
from django.contrib.auth.models import User


class WorkFlow(models.Model):
    """
        Store the group related information
    """
    # TODO Add other details also
    group = models.ForeignKey(Groups)


class WorkFlowStates(models.Model):
    """
        Store the group related information
    """
    workflow = models.ForeignKey(WorkFlow)
    state = models.CharField(max_length=127)
    previous_state = models.ForeignKey('self', null=True, blank=True, related_name='previous')
    next_state = models.ForeignKey('self', null=True, blank=True, related_name='next')


class Tasks(models.Model):
    group = models.ForeignKey(Groups)
    name = models.CharField(max_length=511)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='created_by')
    assigned_by = models.ForeignKey(User, related_name='assigned_by')
    assigned_to = models.ForeignKey(User, related_name='assigned_to')
    status = models.ForeignKey(WorkFlowStates)
