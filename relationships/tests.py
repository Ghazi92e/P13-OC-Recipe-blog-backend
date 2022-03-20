from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from relationships.models import Relationships
from relationships.serializers import RelationshipsSerializer
from recipes.serializers import RecipesSerializer
from categories.models import Categories
from uploadfile.models import Uploadfile
from rest_framework.test import APITestCase
from recipes.models import Recipes

User = get_user_model()
class RelationshipsTests(APITestCase):

    def setUp(self):
        self.relationships_path = '/api-relationships/'

        file = Uploadfile.objects.create(file="url_image")

        self.user1 = User.objects.create_user(username='User1', email='user1@mail.com', password='user123', file=file, image_url='user_image_url')
        self.user2 = User.objects.create_user(username='User2', email='user2@mail.com', password='user1234', file=file, image_url='user_image_url2')

        self.client.force_authenticate(user=self.user1)
        self.client.force_authenticate(user=self.user2)

        self.relationships = Relationships.objects.create()
        self.relationships.user_follower.add(self.user1)
        self.relationships.user_following.add(self.user2)

    def test_can_create_relationships(self):
        serializer = RelationshipsSerializer(self.relationships)
        request = self.client.post(self.relationships_path, serializer.data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_can_delete_relationships(self):
        pk = self.relationships.pk
        response = self.client.delete(self.relationships_path + str(pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)