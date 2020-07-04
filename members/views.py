"""Views for the members app"""
from rest_framework import viewsets
from django.http import HttpResponse

from .serializers import UserSerializer, ActivitySerializer
from .models import User, ActivityPeriod

# Create your views here.
def index(request):
    """Index function for main page view"""
    return HttpResponse("Hello, user. You are at members index.")


# ActivityPeriod APIView class
class ActivityPeriodView(viewsets.ModelViewSet):
    """A class for ActivityPeriod APIView"""

    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivitySerializer(many=True)


# User APIView class
class UserProfile(viewsets.ModelViewSet):
    """A class for User APIView using UserSerializer"""

    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
