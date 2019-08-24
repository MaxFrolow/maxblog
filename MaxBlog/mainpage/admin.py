from django.contrib import admin


from .models import Post, Comment

@admin.register(Post)
class MainpageAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_datetime', 'update_datetime', 'id']
    list_filter = ['created_datetime', 'update_datetime']
    search_fields = ['title', 'text', 'id']

@admin.register(Comment)
class MainpageAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_datetime', 'id']
    list_filter = ['created_datetime']
    search_fields = ['post', 'author', 'id']