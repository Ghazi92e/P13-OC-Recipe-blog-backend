from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from recipes.serializers import RecipesSerializer
from categories.models import Categories
from uploadfile.models import Uploadfile
from recipes.models import Recipes

User = get_user_model()


class RecipesTests(APITestCase):

    def setUp(self):
        self.recipes_path = '/api/recipes/'

        file = Uploadfile.objects.create(file="url_image")
        cat1 = Categories.objects.create(name="TestCategory")

        user = User.objects.create_user(username='User1',
                                        email='user1@mail.com',
                                        password='user123', file=file,
                                        image_url='user_image_url')
        self.client.force_authenticate(user=user)
        self.recipe = Recipes.objects.create(title='Recette1',
                                             ingredients='Ingredients1',
                                             description='Description1',
                                             file=file, user=user,
                                             category=cat1,
                                             image_url='http://127.0.0.1:8000/media/recipes1')

    def test_can_create_recipe(self):
        serializer = RecipesSerializer(self.recipe)
        request = self.client.post(self.recipes_path, serializer.data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_can_update_recipe(self):
        serializer = RecipesSerializer(self.recipe)
        pk = self.recipe.pk
        response = self.client.put(self.recipes_path + str(pk) + '/',
                                   serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_recipe(self):
        response = self.client.get(self.recipes_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_can_read_recipe_detail(self):
        pk = self.recipe.pk
        response = self.client.get(self.recipes_path + str(pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_recipe(self):
        pk = self.recipe.pk
        response = self.client.delete(self.recipes_path + str(pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
