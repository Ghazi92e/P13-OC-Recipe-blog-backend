from rest_framework import viewsets
from recipes.models import Recipes
from recipes.serializers import RecipesSerializer



class RecipeViewSet(viewsets.ModelViewSet):

    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
    filterset_fields = ['category', 'category__name', 'user', 'user__username']