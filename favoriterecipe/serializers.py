from rest_framework import serializers
from recipes.serializers import RecipesSerializer
from favoriterecipe.models import FavoriteRecipe


class FavoriteRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteRecipe
        fields = ['id', 'user', 'recipe']


class UserFavoriteRecipesSerializer(serializers.ModelSerializer):
    recipe = RecipesSerializer()

    class Meta:
        model = FavoriteRecipe
        fields = ['id', 'user', 'recipe']
