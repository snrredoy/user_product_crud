from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView , TokenVerifyView

app_name = 'customAbstractUser'

urlpatterns = [
    path('signup/' , views.SignUpAPIView.as_view() , name='signup'),

    path('signin/' , TokenObtainPairView.as_view() , name='token_obtain_pair'),
    path('token/refresh/' , TokenRefreshView.as_view() , name='token_refresh'),
    path('token/verify/' , TokenVerifyView.as_view() , name='token_verify'),
    path('home/' , views.HomeAPIView.as_view() , name='home')
]