from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from TestAuth.permissions import IsAuthenticatedOrCreate, IsOwnerOrReadOnly
from TestAuth.serializers import UserSerializer, GroupSerializer

from Applicants.models import MyUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrCreate, IsOwnerOrReadOnly)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
