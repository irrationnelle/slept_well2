from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from TestAuth.permissions import IsAuthenticatedOrCreate
from TestAuth.serializers import UserSerializer, GroupSerializer

from Applicants.models import MyUser


# 사용자 목록을 화면에 뿌려주는 ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrCreate,)


# 그룹목록을 화면에 뿌려주는 ViewSet
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
