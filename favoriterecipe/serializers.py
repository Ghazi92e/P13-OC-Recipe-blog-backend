from django.db.models import fields
from rest_framework import serializers
from favoriterecipe.models import FavoriteRecipe


class FavoriteRecipeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FavoriteRecipe
        fields = ['id', 'user', 'recipe']