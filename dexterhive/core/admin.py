from django.contrib import admin
from dexterhive.core import models

admin.site.register(models.UserProfile)
admin.site.register(models.Invites)
admin.site.register(models.Groups)
