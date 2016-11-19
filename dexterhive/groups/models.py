from __future__ import unicode_literals

import uuid
from django.db import models
from dexterhive.core.models import ModelBase


class Groups(ModelBase):
    """
        Store the group related information
    """
    uuid = models.UUIDField(default=uuid.uuid4)
    avatar = models.URLField(null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    name = models.CharField(max_length=127, default="")
    description = models.TextField(null=True)
    type = models.CharField(max_length=63, default="")
    visibility = models.CharField(max_length=15, default="Public")
