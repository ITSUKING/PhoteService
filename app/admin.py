# Register your models here.
from django.contrib import admin

from app.models import Photo, Category


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Category, CategoryAdmin)
