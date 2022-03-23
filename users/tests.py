from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from favoriterecipe.models import FavoriteRecipe
from favoriterecipe.serializers import FavoriteRecipeSerializer
from users.serializers import UsersSerializer
from recipes.serializers import RecipesSerializer
from categories.models import Categories
from uploadfile.models import Uploadfile
from rest_framework.test import APITestCase
from recipes.models import Recipes

User = get_user_model()
class UsersTests(APITestCase):

    def setUp(self):
        self.users_path = '/api-users/'

        file = Uploadfile.objects.create(file="url_image")
        cat1 = Categories.objects.create(name="TestCategory")

        self.user = User.objects.create_user(username='test1', email='test1@mail.com', password='user123', file=file, image_url='http://127.0.0.1:8000/media/user1')
        self.client.force_authenticate(user=self.user)
        self.recipe = Recipes.objects.create(title='Recette1', ingredients='Ingredients1', description='Description1', file=file, user=self.user, category=cat1, image_url='http://127.0.0.1:8000/media/recipes1')

    def test_can_create_user(self):
        file1 = Uploadfile.objects.create(file="url_image")
        self.user1 = {
            "username": "user1",
            "email": "user1@mail.com",
            "password": "user123",
            "file": file1.id,
            "image_url": "http://127.0.0.1:8000/media/user1"
        }
        request = self.client.post(self.users_path, self.user1)
        print(request.content)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)


    def test_can_update_user(self):
        serializer = UsersSerializer(self.user)
        pk = self.user.pk
        response = self.client.put(self.users_path + str(pk) + '/', serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_user(self):
        response = self.client.get(self.users_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_can_read_recipe_detail(self):
        pk = self.user.pk
        response = self.client.get(self.users_path + str(pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_recipe(self):
        pk = self.user.pk
        response = self.client.delete(self.users_path + str(pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_can_read_user_favorite_recipes(self):
        pk = self.user.pk
        response = self.client.get(self.users_path + str(pk) + '/favorite_recipes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_can_create_user_favorite_recipes(self):
        user_favorite_recipes = {
            "user": self.user.pk,
            "recipe": self.recipe.pk
        }
        response = self.client.post(self.users_path + str(self.user.pk) + '/favorite_recipes/', user_favorite_recipes)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_can_delete_user_favorite_recipes(self):
        user_favorite_recipes = {
            "user": self.user.pk,
            "recipe": self.recipe.pk
        }
        self.client.post(self.users_path + str(self.user.pk) + '/favorite_recipes/', user_favorite_recipes)

        response_delete = self.client.delete(self.users_path + str(self.user.pk) + '/favorite_recipes/', user_favorite_recipes)
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)


