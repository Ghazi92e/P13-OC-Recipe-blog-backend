from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_receiver')
    message = models.TextField()

    class Meta:
        ordering = ['created']
