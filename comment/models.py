from django.contrib.auth import get_user_model
from django.db import models

from django.contrib.auth.models import User

User = get_user_model()

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']