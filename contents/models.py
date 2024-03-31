from django.db import models
from customers.models import Account
from django.utils import timezone
from dateutil.relativedelta import relativedelta





class Channel(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    display_picture = models.ImageField(upload_to='channel_display_pictures/', null=True, blank=True)
    cover_photo = models.ImageField(upload_to='channel_cover_photos/', null=True, blank=True)
    description = models.TextField(blank=True)
    email_address = models.EmailField()
    followers = models.ManyToManyField(Account, related_name='following_list', blank=True)
    
    notification_options = models.TextField(blank=True)
    verified_profile = models.ForeignKey(Account, on_delete=models.CASCADE)


class Collaborator(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    administrative_privilege = models.CharField(max_length=100)


class BroadCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    broad_category = models.ForeignKey(BroadCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class VideoContent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    sources = models.TextField()
    date_time = models.DateTimeField()
    place = models.CharField(max_length=255) 
    broad_categories = models.ManyToManyField(BroadCategory, related_name='video_contents')
    sub_categories = models.ManyToManyField(SubCategory, related_name='video_contents')
    keywords = models.TextField()
    follow_up_link = models.URLField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    upload_channels = models.TextField()
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title
