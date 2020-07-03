from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=10)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=200)
    def __str__(self):
        return self.user_id + ' : ' + self.real_name

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')
