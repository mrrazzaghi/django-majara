from django.contrib import admin
from django.utils.html import format_html

from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):

    def pictureShow(self, obj):
        if obj.image == None:
            return "بدون عکس"
        else:
            return format_html("<img src='%s' height=50px>" % obj.image.url)

    list_display_links = ("title", "pictureShow", "slug")
    list_display = ("title", "pictureShow", "slug")
    search_fields = ['slug', 'title']

    pictureShow.allow_tags = True

admin.site.register(Category, CategoryAdmin)
admin.site.register(Story)
admin.site.register(DialogStory)
admin.site.register(Author)
admin.site.register(TextStory)
