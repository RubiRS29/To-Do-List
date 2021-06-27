from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.


class CustomUserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + ((None, {'fields': ('pic_choice',)}),)
    add_fieldsets = BaseUserAdmin.add_fieldsets + ((None, {'fields': ('pic_choice',)}),)


admin.site.register(User, CustomUserAdmin)
