from django.urls import path
from .views import WebNewsView, NewsItemCreateView

urlpatterns = [
    path('', WebNewsView.as_view(), name='home'),
    path('create/', NewsItemCreateView.as_view(), name='news_item_create'),
    # path('news/<int:item_id>/', NewsDetailsView.as_view(), name='news-detail'),
]