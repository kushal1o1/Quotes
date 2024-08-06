# admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import UserInfo, Video, Quote, ImagePost

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture_display', 'bio', 'website')
    search_fields = ('user__username', 'bio', 'website')
    list_filter = ('user',)
    readonly_fields = ('user', 'profile_picture_display')

    def profile_picture_display(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="100" height="100"/>', obj.profile_picture.url)
        return 'No image'
    profile_picture_display.short_description = 'Profile Picture'

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'posted_date', 'video_id', 'video_file')
    search_fields = ('title', 'description', 'user__username')
    list_filter = ('posted_date', 'user')
    readonly_fields = ('video_id',)
    ordering = ('-posted_date',)

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'quote', 'posted_date')
    search_fields = ('quote', 'user__username')
    list_filter = ('posted_date', 'user')
    ordering = ('-posted_date',)

@admin.register(ImagePost)
class ImagePostAdmin(admin.ModelAdmin):
    list_display = ('user', 'imgfile_display', 'posted_date')
    search_fields = ('user__username',)
    list_filter = ('posted_date', 'user')
    ordering = ('-posted_date',)

    def imgfile_display(self, obj):
        if obj.imgfile:
            return format_html('<img src="{}" width="100" height="100"/>', obj.imgfile.url)
        return 'No image'
    imgfile_display.short_description = 'Image'
