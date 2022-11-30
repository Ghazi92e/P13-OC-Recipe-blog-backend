import json
from rest_framework import viewsets
from rest_framework import permissions
from user_tchat.models import Message
from user_tchat.serializers import MessageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class UserTchatViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @action(detail=False, methods=['get'])
    def current_user_tchat(self, request):
        getusertchatparam = request.query_params.get('users-tchat')
        paramtolist = json.loads(getusertchatparam)
        queryset = Message.objects.filter(sender__in=paramtolist, receiver__in=paramtolist)
        if request.method == 'GET':
            serializer = MessageSerializer(queryset, many=True)
            return Response(serializer.data)