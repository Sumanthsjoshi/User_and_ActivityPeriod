"""models for members app"""
from django.db import models

# Create your models here.
class ActivityPeriod(models.Model):
    """Activity period model"""
    id = models.CharField(max_length=10, primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.id


class User(models.Model):
    """User model"""
    id = models.CharField(max_length=10, primary_key=True)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=200)
    activity_periods = models.ForeignKey(ActivityPeriod, on_delete=models.CASCADE, null=True)
