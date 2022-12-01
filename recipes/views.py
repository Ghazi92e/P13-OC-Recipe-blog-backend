from rest_framework import viewsets
from recipes.models import Recipes
from recipes.serializers import RecipesSerializer
from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if (request.user.is_superuser is True):
            return True

        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            # Instance must have an attribute named `user`.
            return obj.user == request.user


class RecipeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsUserOrReadOnly]
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
    filterset_fields = ['category', 'category__name', 'user', 'user__username']
