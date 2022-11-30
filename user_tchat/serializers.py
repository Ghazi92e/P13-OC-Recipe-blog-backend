from rest_framework import serializers
from users.serializers import UsersSerializer
from user_tchat.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'created', 'message', 'sender', 'receiver']