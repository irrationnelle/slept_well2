from django.contrib.auth.models import User, Group
from rest_framework import serializers

from Applicants.models import MyUser


# 사용자 목록
class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = MyUser.objects.create(
            email=validated_data['email'],
            nickname=validated_data['nickname']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = MyUser
        fields = ('url', 'email', 'nickname', 'password')


# 사용자 그룹
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
