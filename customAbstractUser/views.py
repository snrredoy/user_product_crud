from django.shortcuts import render 
from .models import CustomAbstractBaseUser
from .serializers import SignUpSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class SignUpAPIView(APIView):
    permission_classes = []

    def post(self, request):
        data = request.data

        password = data.get('password', None)
        confirm_password = data.get('confirm_password', None)

        if password != confirm_password:
            raise ValidationError('Passwords do not match')

        serializer = SignUpSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def get(self, request):
        users = CustomAbstractBaseUser.objects.all()
        serializer = SignUpSerializer(users, many=True)
        return Response(serializer.data)
    

class HomeAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, SNR!'}
        return Response(content)