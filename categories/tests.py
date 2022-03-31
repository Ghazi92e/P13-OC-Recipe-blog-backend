from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from categories.serializers import CategoriesSerializer
from categories.models import Categories
from uploadfile.models import Uploadfile
from rest_framework.test import APITestCase

User = get_user_model()
class CategoriesTests(APITestCase):

    def setUp(self):
        self.categories_path = '/api/categories/'

        file = Uploadfile.objects.create(file="url_image")
        self.cat = Categories.objects.create(name="TestCategory")

        user = User.objects.create_user(username='User1', email='user1@mail.com', password='user123', file=file, image_url='user_image_url')
        self.client.force_authenticate(user=user)

    def test_can_create_category(self):
        serializer = CategoriesSerializer(self.cat)
        request = self.client.post(self.categories_path, serializer.data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)


    def test_can_update_category(self):
        serializer = CategoriesSerializer(self.cat)
        pk = self.cat.pk
        response = self.client.put(self.categories_path + str(pk) + '/', serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_category(self):
        response = self.client.get(self.categories_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_can_read_category_detail(self):
        pk = self.cat.pk
        response = self.client.get(self.categories_path + str(pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_category(self):
        pk = self.cat.pk
        response = self.client.delete(self.categories_path + str(pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
