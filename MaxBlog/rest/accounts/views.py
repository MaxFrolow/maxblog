from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser
from rest.accounts.serializers import CreateUserSerializer
from rest_framework import viewsets


User = get_user_model()
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (IsAdminUser, )


