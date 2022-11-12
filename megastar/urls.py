"""
megastar URL Configuration
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from mainapp.views import WriterViewSet
# Create your views here.

urlpatterns = [
    path('admin/', admin.site.urls),
]
router = DefaultRouter()
router.register(r'writers', WriterViewSet, basename='writers')

urlpatterns += router.urls


