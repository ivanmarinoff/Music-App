from django.contrib import admin
from django.utils.html import format_html

from .models import Profile, Album


class imageAdmin(admin.ModelAdmin):
    list_display = ["album_name", "artist", "genre", "description", "image_url", "image_tag", "price"]
    list_filter = ["album_name", "artist", "genre"]
    search_fields = ['album_name']
    ordering = ['-album_name']

    def image_tag(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.image_url))
        return None


class UserModelAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "age", "image_url", "image_tag"]
    list_filter = ["username", "email", "age"]
    search_fields = ['username']
    ordering = ['-username']

    def image_tag(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.image_url))
        return None


admin.site.register(Album, imageAdmin)
admin.site.register(Profile, UserModelAdmin)
