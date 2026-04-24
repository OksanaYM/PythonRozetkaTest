from django.contrib.auth import get_user_model
from django.db.transaction import atomic
from rest_framework import serializers

from apps.core.enums.regex_enum import RegexEnum
from apps.user.models import ProfileModel
from django.core import validators as V

from apps.user.services.email_service import EmailService

UserModel = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age', 'created_at', 'updated_at')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[
            V.RegexValidator(RegexEnum.PASSWORD.pattern, RegexEnum.PASSWORD.msg)
        ])


    class Meta:
        model = UserModel
        fields = (
            'id',
            'email',
            'password',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'created_at',
            'updated_at',
            'profile',
        )
        read_only_fields = (
            'id',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'created_at',
            'updated_at',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }


    @atomic
    def create(self, validated_data:dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(user=user, **profile)
        EmailService.register(user)
        return user