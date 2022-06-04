from rest_framework import serializers

from uploadfile.models import Uploadfile


class UploadfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Uploadfile
        fields = ['id', 'file']
