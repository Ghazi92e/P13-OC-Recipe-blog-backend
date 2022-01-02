from django.shortcuts import render
from rest_framework import viewsets
from favorite_recipe.models import FavoriteRecipe
from favorite_recipe.serializers import FavoriteRecipeSerializer



class FavoriteRecipeViewSet(viewsets.ModelViewSet):
    
    queryset = FavoriteRecipe.objects.all()
    serializer_class = FavoriteRecipeSerializer