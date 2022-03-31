from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from favoriterecipe.serializers import FavoriteRecipeSerializer
from favoriterecipe.models import FavoriteRecipe
from categories.models import Categories
from uploadfile.models import Uploadfile
from rest_framework.test import APITestCase
from recipes.models import Recipes

User = get_user_model()
class FavoriteRecipeTests(APITestCase):

    def setUp(self):
        self.favoriterecipe_path = '/api/favoriterecipe/'
    
        file = Uploadfile.objects.create(file="url_image")
        cat1 = Categories.objects.create(name="TestCategory")

        user = User.objects.create_user(username='User1', email='user1@mail.com', password='user123', file=file, image_url='user_image_url')
        self.client.force_authenticate(user=user)
    
        self.recipe = Recipes.objects.create(title='Recette1', ingredients='Ingredients1', description='Description1', file=file, user=user, category=cat1, image_url='http://127.0.0.1:8000/media/recipes1')

        self.favoriterecipe = FavoriteRecipe.objects.create(user=user, recipe=self.recipe)

    def test_can_create_favoriterecipe(self):
        serializer = FavoriteRecipeSerializer(self.favoriterecipe)
        request = self.client.post(self.favoriterecipe_path, serializer.data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)


    def test_can_update_favoriterecipe(self):
        serializer = FavoriteRecipeSerializer(self.favoriterecipe)
        pk = self.favoriterecipe.pk
        response = self.client.put(self.favoriterecipe_path + str(pk) + '/', serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_favoriterecipe(self):
        response = self.client.get(self.favoriterecipe_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_can_read_favoriterecipe_detail(self):
        pk = self.favoriterecipe.pk
        response = self.client.get(self.favoriterecipe_path + str(pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_favoriterecipe(self):
        pk = self.favoriterecipe.pk
        response = self.client.delete(self.favoriterecipe_path + str(pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

