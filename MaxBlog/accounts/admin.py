from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'date_added', 'is_active', 'id']
    list_filter = ['is_active', 'date_added']
    search_fields = ['email', 'first_name', 'last_name', 'date_added', 'id']
