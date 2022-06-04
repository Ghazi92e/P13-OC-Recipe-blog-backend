from django.db import models
from django.contrib.auth import get_user_model
from recipes.models import Recipes

User = get_user_model()


class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE,
                               related_name='user_favorite_recipes')
