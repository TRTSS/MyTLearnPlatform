from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['username', 'surname', 'firstname', 'lastname', 'email', 'role']
    list_filter = ['role', 'surname']
