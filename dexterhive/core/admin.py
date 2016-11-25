from django.contrib import admin
from dexterhive.core import models

admin.site.register(models.UserProfile)
admin.site.register(models.Invitees)
admin.site.register(models.UserAccessTokens)
admin.site.register(models.ThirdPartyIntegrations)
admin.site.register(models.UserThirdPartyIntegrationMapping)
