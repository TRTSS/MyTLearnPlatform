from django.contrib import admin
from .models import WorkGroup, WorkDay, Department
# Register your models here.
admin.site.register(WorkGroup)
admin.site.register(WorkDay)
admin.site.register(Department)