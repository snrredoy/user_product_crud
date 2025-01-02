from django.db import models
# from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from .managers import CustomUserManager
from django.utils import timezone



# Create your models here.
# class CustomAbstractUser(AbstractUser):
#     username = None
#     email = models.EmailField(("Email Address"), unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email



class CustomAbstractBaseUser(AbstractBaseUser , PermissionsMixin):
    first_name = models.CharField(("First Name "), max_length=30 , blank=True)
    last_name = models.CharField(("Last Name "), max_length=30 , blank=True)
    email = models.EmailField(("Email Address "), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email