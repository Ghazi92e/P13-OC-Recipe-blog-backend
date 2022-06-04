from rest_framework import serializers
from django.contrib.auth import get_user_model
from recipes.serializers import RecipesSerializer, RecipesUsernameImageSerializer

User = get_user_model()


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password',
                  'file', 'image_url', 'is_superuser']

        extra_kwargs = {
            'is_superuser': {'read_only': True},
        }


class UsersFavoriteRecipesSerializer(serializers.ModelSerializer):
    favorite_recipes = RecipesUsernameImageSerializer(many=True,
                                                      read_only=True)

    class Meta:
        model = User
        fields = ['id', 'favorite_recipes', 'username']


class UsersRecipesSerializer(serializers.ModelSerializer):
    user_recipes = RecipesSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'user_recipes', 'username']

# class UsersFollowingSerializer(serializers.ModelSerializer):
#     user_follower_data = RelationshipsUserFollowing(many=True,
#                                                     read_only=True)

#     class Meta:
#         model = User
#         fields = ['id', 'user_follower_data']


class UsersFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'file',
                  'image_url', 'is_superuser', 'user_followings']
