from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_user(
      validated_data['username'],
      validated_data['email'],
      validated_data['password']
    )
    
    Profile.objects.create(user=user) # Create Profile object (with default entries) for the new User

    # print(f"RegisterSeralizer - username: ${validated_data['username']}")
    return user


# Login Serializer
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active: # all included in django by default
      return user
    raise serializers.ValidationError("Incorrect Credentials")


# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Profile
    # fields = '__all__'
    fields = ('image', 'location')


# User Serializer
class UserSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer()

  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'profile')
    
    