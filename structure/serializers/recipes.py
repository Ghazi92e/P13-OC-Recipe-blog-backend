from django.db.models import fields
from rest_framework import serializers
from recipes.models import Recipes


class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ['id', 'title', 'description', 'category', 'file', 'user', 'image_url']