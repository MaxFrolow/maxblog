from django.contrib import admin


from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_datetime', 'update_datetime', 'id']
    list_filter = ['created_datetime', 'update_datetime']
    search_fields = ['title', 'text', 'id']