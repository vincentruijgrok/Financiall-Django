"""
URL configuration for Financiall project.

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('allauth.urls')),
    path('', include('core.urls'))
]
