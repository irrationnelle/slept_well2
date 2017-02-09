from django.contrib.auth.models import User, Group
from rest_framework import serializers

from Applicants.models import MyUser


# 사용자 목록
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('url', 'email', 'nickname')


# 사용자 그룹
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
