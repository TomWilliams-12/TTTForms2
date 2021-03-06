from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile

class UserAdminConfig(UserAdmin):

    search_fields = ('email', 'user_name', 'first_name')
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('-first_name',)
    list_display = ('email', 'user_name', 'first_name', 'is_active', 'is_staff', 'is_auditor')

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_auditor')}),
        ('Personal', {'fields': ('reg', 'signature')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'user_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_auditor')
        }),
    )


admin.site.register(Profile, UserAdminConfig)
