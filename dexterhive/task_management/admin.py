from django.contrib import admin
from dexterhive.task_management import models
from related_admin import RelatedFieldAdmin

admin.site.register(models.WorkFlow)
admin.site.register(models.Tasks)


class WorkFlowStatesAdmin(RelatedFieldAdmin):
    list_display = ("state", "previous_state__state", "next_state__state")


admin.site.register(models.WorkFlowStates, WorkFlowStatesAdmin)
