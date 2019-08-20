from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    def pictureShow(self, obj):
        if obj.image is None:
            return 'بدون عکس'
        else:
            return format_html("<img src='%s' height=50px>" % obj.image.url)

    list_display_links = ('title', 'pictureShow', 'slug')
    list_display = ('title', 'pictureShow', 'slug')
    search_fields = ['slug', 'title']

    pictureShow.allow_tags = True


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):

    def pictureShow(self, obj):
        if obj.image is None:
            return 'بدون عکس'
        else:
            return format_html("<img src='%s' height=50px>" % obj.image.url)

    list_display = ('title', 'pictureShow', 'slug')
    list_display_links = ('title', 'pictureShow', 'slug')
    search_fields = ['slug', 'title']

    pictureShow.allow_tags = True


@admin.register(DialogStory)
class DialogStoryAdmin(admin.ModelAdmin):

    def pictureShow(self, obj):
        if obj.image is None:
            return 'بدون عکس'
        else:
            return format_html("<img src='%s' height=50px>" % obj.image.url)

    list_display = ('storyId', 'pictureShow', 'dialogTextType')
    list_display_links = ('storyId', 'pictureShow', 'dialogTextType')
    search_fields = ['storyId', 'dialogTextType']

    pictureShow.allow_tags = True


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    def pictureShow(self, obj):
        if obj.avatar is None:
            return 'بدون عکس'
        else:
            return format_html("<img src='%s' height=50px>" % obj.avatar.url)

    list_display_links = ('FirstName', 'LastName', 'pictureShow')
    list_display = ('FirstName', 'LastName', 'pictureShow')
    search_fields = ['FirstName', 'LastName']

    pictureShow.allow_tags = True


@admin.register(TextStory)
class TextStoryAdmin(admin.ModelAdmin):
    list_display_links = ('storyId',)
    list_display = ('storyId',)
    search_fields = ['storyId', 'pageNumber']
