from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from user_tchat.serializers import MessageSerializer
from user_tchat.models import Message
from uploadfile.models import Uploadfile

User = get_user_model()


class UserTchatTests(APITestCase):

    def setUp(self):
        self.user_message_path = '/api/user-tchat/'
        file = Uploadfile.objects.create(file="url_image")
        user_sender = User.objects.create_user(username='User1',
                                        email='user1@mail.com',
                                        password='user123', file=file,
                                        image_url='user_image_url')
        user_receiver = User.objects.create_user(username='User2',
                                        email='user2@mail.com',
                                        password='user321', file=file,
                                        image_url='user_image_url')
        self.client.force_authenticate(user=user_sender)
        self.client.force_authenticate(user=user_receiver)
        self.usermessage = Message.objects.create(message='NewMessage',
                                             sender=user_sender,
                                             receiver=user_receiver)
        user_message_sender = self.usermessage.sender.pk
        user_message_receiver = self.usermessage.receiver.pk
        self.get_current_users_tchat = f'/api/user-tchat/current_user_tchat/?users-tchat=[{user_message_sender},{user_message_receiver}]'


    def test_can_create_message(self):
        serializer = MessageSerializer(self.usermessage)
        request = self.client.post(self.user_message_path, serializer.data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_can_read_user_message(self):
        response = self.client.get(self.user_message_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_can_read_user_message_detail(self):
        pk = self.usermessage.pk
        response = self.client.get(self.user_message_path + str(pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_current_users_messages(self):
        response = self.client.get(self.get_current_users_tchat)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    

