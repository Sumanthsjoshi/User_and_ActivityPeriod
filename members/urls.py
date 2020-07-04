"""members app URL Configuration"""
from django.urls import path, include
from rest_framework import routers
from .views import UserProfile

# router set up for members app
ROUTER = routers.DefaultRouter()
ROUTER.register(r'members', UserProfile)

urlpatterns = [
    path('', include(ROUTER.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
