from rest_framework import viewsets
from categories.serializers import CategoriesSerializer
from categories.models import Categories


class CategoriesViewSet(viewsets.ModelViewSet):

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
