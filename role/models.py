from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

User = get_user_model()

class Role(models.Model):
    title = models.CharField(max_length=50)
    user = models.ManyToManyField(User)