import io
import os
from PIL import Image
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from blog_lebanese_recipes.settings import BASE_DIR
from uploadfile.models import Uploadfile
from rest_framework.test import APITestCase

User = get_user_model()
class UploadfileTests(APITestCase):

    def setUp(self):
        self.uploadfile_path = '/api-upload-file/'

        self.file = Uploadfile.objects.create(file="http://127.0.0.1:8000/media/recipes1")

        user = User.objects.create_user(username='User1', email='user1@mail.com', password='user123', file=self.file, image_url='user_image_url')
        self.client.force_authenticate(user=user)
    

    def generate_photo_file(self):
        file = io.BytesIO(b'test')
        return file

    def test_can_create_uploadfile(self):
        photo_file = self.generate_photo_file()
        data = {
                'file':photo_file
            }
        request = self.client.post(self.uploadfile_path, data, format='multipart')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_can_delete_uploadfile(self):
        pk = self.file.pk
        response = self.client.delete(self.uploadfile_path + str(pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
