# admin.py
from django.contrib import admin
from app_users.models import CustomUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)