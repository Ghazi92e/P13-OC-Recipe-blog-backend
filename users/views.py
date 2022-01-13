from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from uploadfile.models import Uploadfile
from users.serializers import UsersSerializer

User = get_user_model()
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    filterset_fields = ['auth_token', 'id']


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