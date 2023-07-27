from django.contrib import admin
from .models import NewsItem

class NewsItemAdmin(admin.ModelAdmin):
    list_display = (
        'by',
        'item_id',
        'time',
        'title',
        'score',
        'item_type',
        'url',
    )


admin.site.register(NewsItem, NewsItemAdmin)
