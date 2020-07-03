"""A script to define command to populate members to the database"""
import datetime
from datetime import timedelta
from django.core.management.base import BaseCommand
from members.models import User

class Command(BaseCommand):
    """Commands for members app"""
    help = 'Populates the members to the database'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=str, help='User id of the user')
        parser.add_argument('real_name', type=str, help='Real name of the user')
        parser.add_argument('tz', type=str, help='Time Zone')

    def handle(self, *args, **kwargs):
        user_id = kwargs['user_id']
        real_name = kwargs['real_name']
        tzone = kwargs['tz']
        start_time = datetime.datetime.now()
        end_time = start_time + timedelta(days=1)

        user = User(user_id=user_id, real_name=real_name, tz=tzone)
        user.save()

        user = User.objects.get(user_id=user_id)
        activity_period = user.activityperiod_set.create(start_time=start_time, end_time=end_time)
        activity_period.save()
