from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'email',
        'role'
    )
    list_filter = ('role',)
    model = CustomUser
