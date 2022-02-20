import operator
from functools import reduce
from multiprocessing import Value
from unicodedata import category
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from recipes.serializers import RecipesSerializer, RecipesUsernameImageSerializer
from recipes.models import Recipes
from relationships.models import Relationships
from relationships.serializers import RelationshipsSerializer, RelationshipsUserFollowing
from favoriterecipe.serializers import FavoriteRecipeSerializer, UserFavoriteRecipesSerializer
from favoriterecipe.models import FavoriteRecipe
from uploadfile.models import Uploadfile
from users.serializers import UsersSerializer
from rest_framework.decorators import action

User = get_user_model()
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    filterset_fields = ['auth_token', 'id', 'username']


    def perform_create(self, serializer):
        if serializer.is_valid():
            username = serializer.data.get('username')
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            file_id = serializer.data.get('file')
            image_url = serializer.data.get('image_url')
            file = Uploadfile.objects.get(pk=file_id)
            user = User.objects.create_user(username, email, password, file, image_url)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['get', 'post', 'delete'])
    def favorite_recipes(self, request, pk):
        queryset = FavoriteRecipe.objects.filter(user=pk)
        if request.method == 'GET':
            serializer = UserFavoriteRecipesSerializer(queryset, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = FavoriteRecipeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            querysetdata = FavoriteRecipe.objects.get(user=pk, recipe=request.data.get('recipe'))
            querysetdata.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    

    # @action(detail=True, methods=['get'])
    # def recipes(self, request, pk):
    #     queryset = User.objects.get(pk=pk)
    #     if request.method == 'GET':
    #         serializer = UsersRecipesSerializer(queryset)
    #         return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def recipes(self, request, pk):
        queryset = Recipes.objects.filter(user=pk)
        if request.method == 'GET':
            serializer = RecipesUsernameImageSerializer(queryset, many=True)
            return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def recipes_user_following(self, request):
        usersFollowingsIds = request.data
        print(usersFollowingsIds)
        array = []
        for dataFollow in usersFollowingsIds:
            array.append(dataFollow.get("user_following")[0])
        array.append(dataFollow.get("user_follower")[0])
        print(array)
        queryset = Recipes.objects.filter(user__in=array)
        # queryset = Recipes.objects.filter(title__startswith="Recette")
        if request.method == 'POST':
        #     serializer = UsersRecipesSerializer(queryset)
            serializer = RecipesUsernameImageSerializer(queryset, many=True)
            return Response(serializer.data)

    # @action(detail=False, methods=['post'])
    # def recipes_user_following(self, request):
    #     usersFollowingsIds = request.data
    #     print(usersFollowingsIds)
    #     queryset = Recipes.objects.filter(user__in=usersFollowingsIds)
    #     # queryset = Recipes.objects.filter(title__startswith="Recette")
    #     if request.method == 'POST':
    #         # serializer = UsersRecipesSerializer(queryset)
    #         serializer = RecipesUsernameImageSerializer(queryset, many=True)
    #         return Response(serializer.data)


    @action(detail=False, methods=['post'])
    def get_user_recipes_following_by_category(self, request):
        dict = request.data
        print(dict.get("category__in"), dict.get("user__in"))
        queryset = Recipes.objects.filter(category__in=dict.get("category__in"), user__in=dict.get("user__in"))
        if request.method == 'POST':
            serializer = RecipesUsernameImageSerializer(queryset, many=True)
            return Response(serializer.data)
    
    @action(detail=True, methods=['get', 'post', 'delete'])
    def following(self, request, pk):
        queryset = Relationships.objects.filter(user_follower=pk)
        if request.method == 'GET':
            serializer = RelationshipsUserFollowing(queryset, many=True)
            return Response(serializer.data)
        
        elif request.method == 'POST':
            serializer = RelationshipsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            querysetdata = Relationships.objects.get(user_follower=request.data.get('user_follower'), user_following=request.data.get('user_following'))
            querysetdata.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    

    @action(detail=False, methods=['post'])
    def search_recipes_by_user_followings(self, request):
        dict_recipe_title = request.data
        print(dict_recipe_title.get("title"))
        queryset = Recipes.objects.filter(user__in=dict_recipe_title.get("user__in"), title__startswith=dict_recipe_title.get("title"))
        if request.method == 'POST':
            serializer = RecipesUsernameImageSerializer(queryset, many=True)
            return Response(serializer.data)


        


    # @action(detail=True, methods=['post'])
    # def favorite_recipes(self, request, pk=None):
    #     datatest = User.objects.all().filter(pk=pk)
    #     serializer = UsersFavoriteRecipesSerializer(datatest, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=['put'])
    # def delete_favorite_recipes(self, request, pk=None):
    #     user_recipe = FavoriteRecipe.objects.all().filter(user=pk).first()
    #     serializer = FavoriteRecipeSerializer(user_recipe, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        # favorite_recipes = user_recipe.favorite_recipes.all()
        # remove = request.data['favorite_recipes']
        # datatest.delete()






# @api_view(['GET', 'POST'])
# def users_list(request):        
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UsersSerializer(users, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = UsersSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.data.get('username')
#             email = serializer.data.get('email')
#             password = serializer.data.get('password')
#             user = User.objects.create_user(username, email, password)
#             user.save()
#             # datauser = User.objects.get(auth_token='b3f87da93354fe453b0dc289c8b5b8886b20767e')
#             # print(datauser.id)
#             for user in User.objects.all():
#                 data = Token.objects.get_or_create(user=user)
#                 print(data, user.auth_token.key)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)