from django.contrib import admin


# Register your models here.
from main.models import UserProfile, Event

admin.site.register(UserProfile)
admin.site.register(Event)
