"""Serializers for get_members_api"""
from rest_framework import serializers
from .models import User, ActivityPeriod


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    """Class for ActivityPeriod serializers"""

    # ActivityPeriod Meta fields
    class Meta:
        """Meta class for fields"""
        model = ActivityPeriod
        fields = ('start_time', 'end_time',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Class for User serializers"""

    activity_periods = ActivitySerializer(read_only=True)

    class Meta:
        """Meta class for fields"""
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')
