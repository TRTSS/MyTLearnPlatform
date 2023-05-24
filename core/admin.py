from django.contrib import admin
from .models import WorkGroup, WorkDay, Department, GroupHomeTask
# Register your models here.
admin.site.register(WorkGroup)
admin.site.register(WorkDay)
admin.site.register(Department)
admin.site.register(GroupHomeTask)
