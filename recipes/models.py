from django.contrib.auth import get_user_model
from django.db import models
from uploadfile.models import Uploadfile
from categories.models import Categories
from django.contrib.auth.models import User

User = get_user_model()

class Recipes(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    file = models.ForeignKey(Uploadfile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    class Meta:
        ordering = ['created']