from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

# Create your models here.

class Relationships(models.Model):
    user_follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_follower_data', null=True)
    user_following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_following_data', null=True)
