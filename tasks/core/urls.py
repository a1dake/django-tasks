from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('api_tasks.urls')),
    path('admin/', admin.site.urls),
]
