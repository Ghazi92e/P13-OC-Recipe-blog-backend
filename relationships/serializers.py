from django.db.models import fields
from rest_framework import serializers
from structure.serializers.users import UsersSerializer
from relationships.models import Relationships


class RelationshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationships
        fields = ['id', 'user_follower', 'user_following']


class RelationshipsUserFollowing(serializers.ModelSerializer):
    # user_following = UsersSerializer(many=True, read_only=True)
    class Meta:
        model = Relationships
        fields = ['user_follower', 'user_following']