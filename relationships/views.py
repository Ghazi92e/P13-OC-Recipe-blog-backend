from django.shortcuts import render
from rest_framework import viewsets
from relationships.serializers import RelationshipsSerializer

from relationships.models import Relationships

# Create your views here.

class RelationshipsViewSet(viewsets.ModelViewSet):

    queryset = Relationships.objects.all()
    serializer_class = RelationshipsSerializer
    filterset_fields = ['user_follower', 'user_following']