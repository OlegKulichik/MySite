from django.contrib import admin
from item.models import Item
from django.utils.safestring import mark_safe


class AdminItem(admin.ModelAdmin):
    list_display = ("brend", "model","color", 'get_photo')
    # readonly_fields = ['get_photo',]
    list_filter = ["brend"]
    search_fields = ["brend","model","color"]


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe (f'<img src="{obj.photo.url}" width = 50 height = 50 >')
    get_photo.short_description = 'Логотип'


admin.site.register(Item, AdminItem)
