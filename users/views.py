
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
from users.serializers import UsersFollowingSerializer, UsersSerializer
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

User = get_user_model()

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            print("je suis la ")
            return True
        if obj.id == request.user.id:
            return True
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    filterset_fields = ['auth_token', 'id', 'username']

    def get_permissions(self):
        """
        Permit action create to let user create account.
        """
        permission_classes = []
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated, IsAdminUserOrReadOnly]
        return [permission() for permission in permission_classes]


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

    @action(detail=True, methods=['get'])
    def recipes(self, request, pk):
        queryset = Recipes.objects.filter(user=pk)
        if request.method == 'GET':
            serializer = RecipesUsernameImageSerializer(queryset, many=True)
            return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def recipes_user_following(self, request, pk):
        user_following = []
        queryset = Relationships.objects.filter(user_follower=pk)
        serializer = RelationshipsUserFollowing(queryset, many=True)
        for data in serializer.data:
            user_following.append(data.get('user_following'))
        user_following.append(int(pk))

        print(user_following)
        queryset = Recipes.objects.filter(user__in=user_following)
        # queryset = Recipes.objects.filter(title__startswith="Recette")
        if request.method == 'GET':
            serializer = RecipesUsernameImageSerializer(queryset, many=True)
            return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def get_user_recipes_following_by_category(self, request, pk):
        user_following = []
        queryset = Relationships.objects.filter(user_follower=pk)
        serializer = RelationshipsUserFollowing(queryset, many=True)
        for data in serializer.data:
            user_following.append(data.get('user_following'))
        user_following.append(int(pk))

        dict = request.data
        print(dict.get("category__in"))
        queryset = Recipes.objects.filter(category__in=dict.get("category__in"), user__in=user_following)
        if request.method == 'POST':
            serializer = RecipesUsernameImageSerializer(queryset, many=True)
            return Response(serializer.data)
    
    @action(detail=True, methods=['get', 'post', 'delete'])
    def following(self, request, pk):
        user_following = []
        queryset = Relationships.objects.filter(user_follower=pk)
        if request.method == 'GET':
            serializer = RelationshipsUserFollowing(queryset, many=True)
            for data in serializer.data:
                user_following.append(data.get('user_following'))
            user_following.append(int(pk))
            return Response(user_following)
        
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
    
    @action(detail=True, methods=['get'])
    def follower(self, request, pk):
        user_follower = []
        queryset = Relationships.objects.filter(user_following=pk)
        if request.method == 'GET':
            serializer = RelationshipsUserFollowing(queryset, many=True)
            for data in serializer.data:
                user_follower.append(data.get('user_follower'))
            return Response(user_follower)
    
    @action(detail=True, methods=['get'])
    def count_user_follower(self, request, pk):
        queryset = Relationships.objects.filter(user_following=pk).count()
        if request.method == 'GET':
            return Response(queryset)

    @action(detail=True, methods=['get'])
    def count_user_following(self, request, pk):
        queryset = Relationships.objects.filter(user_follower=pk).count()
        if request.method == 'GET':
            return Response(queryset)
    
    @action(detail=True, methods=['get'])
    def count_user_recipes(self, request, pk):
        queryset = Recipes.objects.filter(user=pk).count()
        if request.method == 'GET':
            return Response(queryset)
    

    # @action(detail=True, methods=['get'])
    # def user_followings(self, request, pk):
    #     queryset = User.objects.filter(pk=pk)
    #     if request.method == 'GET':
    #         serializer = UsersFollowingSerializer(queryset, many=True)
    #         for testdata in serializer.data:
    #             print(testdata.get('user_followings'))
    #         return Response(serializer.data)




