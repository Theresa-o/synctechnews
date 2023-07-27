from django.urls import path
from .views import NewsDetailsView, NewsIdView

urlpatterns = [
    path('', NewsIdView.as_view(), name='index'),
    path('news/<int:item_id>/', NewsDetailsView.as_view(), name='news-detail'),
]
