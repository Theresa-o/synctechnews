from rest_framework import serializers
from .models import NewsItem


class NewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = [
            'by',
            'item_id',
            'time',
            'title',
            'score',
            'item_type',
            'url',
            'api_created',
        ]
