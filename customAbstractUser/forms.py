from django.contrib.auth.forms import UserCreationForm , UserChangeForm
# from .models import CustomAbstractUser
from .models import CustomAbstractBaseUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomAbstractBaseUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomAbstractBaseUser
        fields = ('email',)