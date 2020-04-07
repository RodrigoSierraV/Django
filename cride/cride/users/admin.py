from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from cride.users.models import User, Profile


class CustomUserAdmin(UserAdmin):
    """
        Personalizes Admin for the customized User
    """

    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
        'is_staff',
        'is_client'
    )

    list_filter = (
        'is_client',
        'is_staff',
        'created',
        'modified',
    )

class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'users',
        'reputation',
        'rides_taken',
        'rides_offered'
    )

    search_fields = (
        'users__username',
        'users__email',
        'users__first_name',
        'users__last_name'
    )

    list_filter = ('reputation',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)