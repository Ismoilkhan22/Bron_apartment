from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models

from src.base.models import BaseModel


class UserMG(UserManager):
    def create_user(self, phone=None, password=None, is_staff=False, is_superuser=False, **extra_fields):
        user = self.model(
            phone=phone,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(str(password))
        user.save()
        return user

    def create_superuser(self, phone=None, password=None, **extra_fields):
        return self.create_user(
            phone=phone,
            password=password,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )


class CustomUser(AbstractBaseUser, PermissionsMixin, BaseModel):
    # admin
    fio = models.CharField(max_length=128)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=128, unique=True, )

    # all
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    user_type = models.SmallIntegerField(choices=[
        (1, "Admin"),
        (2, "User"),
    ], default=2)

    objects = UserMG()

    REQUIRED_FIELDS = ['user_type', 'email']
    USERNAME_FIELD = 'phone'
