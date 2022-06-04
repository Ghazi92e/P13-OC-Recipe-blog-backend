from rest_framework import status
from django.contrib.auth import get_user_model
from comment.models import Comment
from comment.serializers import CommentSerializer
from uploadfile.models import Uploadfile
from rest_framework.test import APITestCase

User = get_user_model()


class CommentTests(APITestCase):

    def setUp(self):
        self.comment_path = '/api/comment/'

        file = Uploadfile.objects.create(file="url_image")

        self.user = User.objects.create_user(username='User1',
                                             email='user1@mail.com',
                                             password='user123',
                                             file=file,
                                             image_url='user_image_url')
        self.client.force_authenticate(user=self.user)

        self.comment = Comment.objects.create(description="MyFirstComment",
                                              user=self.user)

    def test_can_create_comment(self):
        serializer = CommentSerializer(self.comment)
        request = self.client.post(self.comment_path, serializer.data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_can_update_comment(self):
        serializer = CommentSerializer(self.comment)
        pk = self.comment.pk
        response = self.client.put(self.comment_path + str(pk) + '/',
                                   serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_comment(self):
        response = self.client.get(self.comment_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_can_read_comment_detail(self):
        pk = self.comment.pk
        response = self.client.get(self.comment_path + str(pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_comment(self):
        pk = self.comment.pk
        response = self.client.delete(self.comment_path + str(pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
