from django.shortcuts import render

from rest_framework import viewsets
from role.models import Role
from role.serializers import RoleSerializer



class RoleViewSet(viewsets.ModelViewSet):

    queryset = Role.objects.all()
    serializer_class = RoleSerializer