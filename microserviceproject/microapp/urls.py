from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'account',AccountUpdateViewset,basename='user')

urlpatterns = [
    path('register/',user_register,name='register'),
    path('password_reset/',password_reset,name='password_reset_request'),
    path('send_otp/',send_otp_request,name='send_otp'),
    path('verify_otp/',verify_otp_request,name='verify_otp'),
    path('',include(router.urls)),
]
