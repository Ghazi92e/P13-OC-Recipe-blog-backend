from rest_framework import viewsets
from favoriterecipe.models import FavoriteRecipe
from favoriterecipe.serializers import FavoriteRecipeSerializer


class FavoriteRecipeViewSet(viewsets.ModelViewSet):

    queryset = FavoriteRecipe.objects.all()
    serializer_class = FavoriteRecipeSerializer
