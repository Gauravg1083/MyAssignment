from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','phone_number','password')
        extra_kwargs = {'password':{'write_only':True}}



class PasswordRestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','phone_number')