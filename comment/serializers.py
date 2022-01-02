from django.db.models import fields
from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['id', 'created', 'description', 'user']