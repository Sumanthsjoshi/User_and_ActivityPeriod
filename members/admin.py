"""A script to register admin users"""
from django.contrib import admin
from .models import User

# Register your models here.
admin.site.register(User)
