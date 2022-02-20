from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

# Create your models here.

class Relationships(models.Model):
    user_follower = models.ManyToManyField(User, related_name='user_follower_data')
    user_following = models.ManyToManyField(User, related_name='user_following_data')
