from django.contrib.auth import get_user_model
from django.db import models

from django.contrib.auth.models import User

from recipes.models import Recipes

User = get_user_model()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
