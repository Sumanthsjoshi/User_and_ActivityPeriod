from django.db import models

# Create your models here.
class User(models.Model):
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=200)

class ActivityPeriod(models.Model):
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')
