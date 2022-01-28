from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from favoriterecipe.serializers import FavoriteRecipeSerializer
from favoriterecipe.models import FavoriteRecipe
from uploadfile.models import Uploadfile
from users.serializers import UsersFavoriteRecipesSerializer, UsersSerializer
from rest_framework.decorators import action


User = get_user_model()
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    filterset_fields = ['auth_token', 'id', 'favorite_recipes']


    def perform_create(self, serializer):
        if serializer.is_valid():
            username = serializer.data.get('username')
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            file_id = serializer.data.get('file')
            file = Uploadfile.objects.get(pk=file_id)
            user = User.objects.create_user(username, email, password, file)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['get', 'post', 'delete'])
    def favorite_recipes(self, request, pk):
        queryset = User.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = UsersFavoriteRecipesSerializer(queryset)
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