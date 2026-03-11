
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apps.core.enums.regex_enum import RegexEnum
from apps.core.models import BaseModel
from apps.user.managers import UserManager

from django.core import validators as V


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'
        ordering = ['-id']

    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'user_profile'
        ordering = ['-id']

    name = models.CharField(max_length=25, validators=[V.RegexValidator(RegexEnum.NAME.pattern, RegexEnum.NAME.msg )])
    surname = models.CharField(max_length=25, validators=[V.RegexValidator(RegexEnum.NAME.pattern, RegexEnum.NAME.msg )])
    age = models.IntegerField(validators=[V.MinValueValidator(15), V.MaxValueValidator(100)])
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')






