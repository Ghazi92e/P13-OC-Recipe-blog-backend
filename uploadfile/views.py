from rest_framework import viewsets
from uploadfile.models import Uploadfile
from uploadfile.serializers import UploadfileSerializer


class UploadfileViewSet(viewsets.ModelViewSet):

    queryset = Uploadfile.objects.all()
    serializer_class = UploadfileSerializer
    filterset_fields = ['id']
