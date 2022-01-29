from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class UsersSerializer(serializers.ModelSerializer):
    user_recipes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'file', 'favorite_recipes', 'user_recipes']


class UsersFavoriteRecipesSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'favorite_recipes']
        