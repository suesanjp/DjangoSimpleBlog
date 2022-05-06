from django.contrib import admin

from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "created_at", "updated_at")
    list_display_links = ("id", "text")


admin.site.register(Blog, BlogAdmin)
