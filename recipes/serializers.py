from django.db.models import fields
from rest_framework import serializers
from structure.serializers import UsersSerializer
from recipes.models import Recipes


class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ['id', 'title', 'description', 'category', 'file', 'user', 'image_url']



class RecipesUsernameImageSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    class Meta:
        model = Recipes
        fields = ['id', 'title', 'description', 'category', 'file', 'user', 'image_url']