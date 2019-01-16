from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='user_profile', on_delete=models.CASCADE, db_index=True)
    firebase_uid = models.CharField(max_length=100, unique=True, db_index=True, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta(object):
        unique_together = ('user', 'firebase_uid')
        ordering = ('-created',)

    def __str__(self):
        return self.user.email

class Event(models.Model):
    user = models.ForeignKey(User, related_name='event', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=1000, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    # models.ForeignKey(UserProfile, related_name='watchlist', on_delete=models.CASCADE)