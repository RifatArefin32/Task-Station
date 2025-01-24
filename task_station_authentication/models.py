from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# class for user profile
class UserProfile(models.Model):
    bio = models.TextField(max_length=500, null=True, blank=True)
    profile_picture = models.ImageField(upload_to=upload_to, blank=True, null=True)
    user = models.OneToOneField(User, related_name='profile')