from django.contrib import admin
from .models import Notice


@admin.register(Notice)
class BlogAdmin(admin.ModelAdmin):
    """blog admin"""
    list_display = ('id', 'content', 'create_time')

    # filter date
    date_hierarchy = 'create_time'
    ordering = ('-create_time',)