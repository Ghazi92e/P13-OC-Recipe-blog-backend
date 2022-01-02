from django.db.models import fields
from rest_framework import serializers
from categories.models import Categories


class CategoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categories
        fields = ['id', 'name']