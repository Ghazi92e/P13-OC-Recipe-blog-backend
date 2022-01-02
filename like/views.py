from rest_framework import viewsets
from like.models import Like
from like.serializers import LikeSerializer



class LikeViewSet(viewsets.ModelViewSet):

    queryset = Like.objects.all()
    serializer_class = LikeSerializer