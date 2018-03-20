from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse_lazy

# Create your models here.

class UserProfile(models.Model):
    # user        = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile') # user.profile 
    # following   = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by') 
    # user.profile.following -- users i follow
    # user.followed_by -- users that follow me -- reverse relationship
    # objects = UserProfileManager() # UserProfile.objects.all()
    # objects = UserProfileManager() # UserProfile.objects.all()
    # abc = UserProfileManager() # UserProfile.abc.all()

    def __str__(self):
        return str(self.following.all().count())

    def get_absolute_url(self):
        return reverse_lazy("profiles-detail", kwargs={"username":self.user.username})
