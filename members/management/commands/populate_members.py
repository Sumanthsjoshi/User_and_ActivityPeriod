from django.core.management.base import BaseCommand
from User_and_ActivityPeriod.members.models import User

class Command(BaseCommand):
    help = 'Populates the members to the database'

    def handle(self, *args, **kwargs):
        pass