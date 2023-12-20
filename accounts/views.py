from .serializer import UserSerializers
from .models import UserAccount
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CreateUser(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        user = UserAccount.objects.get(username=request.user)
        user_data = UserSerializers(user).data
        return Response(user_data)
