from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #to view the api, visit http://127.0.0.1:8000/api/
    path('api/', include('news.urls')),
    #to view the app, visit http://127.0.0.1:8000/
    path('', include('webnews.urls')),
]
