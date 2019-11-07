from django.contrib import admin
from .models import Photo


# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created_at', 'updated_at']
    raw_id_fields = ['author']
    list_filter = ['created_at', 'updated_at', 'author']
    search_Fields = ['text', 'created_at']
    ordering = ['-updated_at', '-created_at']


admin.site.register(Photo, PhotoAdmin)
