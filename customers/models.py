from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
from dateutil.relativedelta import relativedelta

class Account(AbstractUser):
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    #following_list = models.ManyToManyField('content.Channel', related_name='followers', blank=True)
    #saved_content_list = models.ManyToManyField('content.VideoContent', related_name='saved_by', blank=True)
    #watch_history = models.ManyToManyField('content.VideoContent', related_name='watched_by', blank=True)
    notification_options = models.TextField(blank=True)
    insights = models.TextField(blank=True)
    notification_on_activities = models.TextField(blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    nid = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    is_nid_verified = models.BooleanField(default=False)
    credibility_rating = models.FloatField(default=0.0)
    monetization = models.BooleanField(default=False)
    real_name = models.CharField(max_length=255)
    submitted_vs_approved_number = models.IntegerField(default=0)

    
    #channels = models.ManyToManyField('Channel', related_name='created_by', blank=True)
    #fact_checks = models.ManyToManyField('FactCheck', related_name='fact_checked_by', blank=True)
