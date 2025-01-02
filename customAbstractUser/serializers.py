from .models import CustomAbstractBaseUser
from rest_framework import serializers , fields
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAbstractBaseUser
        fields = ('email' , 'password' , 'first_name' , 'last_name' , 'is_staff' , 'is_active' , 'is_superuser' , 'date_joined')
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    def create(self , validated_data):

        if validate_password(validated_data['password']) == None:
            password = make_password(validated_data['password'])

            user = CustomAbstractBaseUser.objects.create(
                email = validated_data['email'],
                password = password
            )
        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAbstractBaseUser
        # fields = ('email' , 'first_name' , 'last_name' , 'is_staff' , 'is_active' , 'is_superuser' , 'date_joined')
        fields = '__all__'