from rest_framework import generics, mixins, permissions, viewsets
from knox.models import AuthToken
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, ProfileSerializer


from rest_framework.response import Response
from rest_framework.views import APIView


from django.contrib.auth.models import User
from .models import Profile



# Register API
class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs): # all the data sent in our post request, headers and data, will be part of the request variable
    serializer = self.get_serializer(data=request.data) # Brad video: https://youtu.be/0d7cIfiydAc?t=1350
    serializer.is_valid(raise_exception=True)
    user = serializer.save() # save user to the User table in the database, see the RegisterSerializer code for details

    token = AuthToken.objects.create(user)
    return Response({
      "user": UserSerializer(
        user, context=self.get_serializer_context()).data,
        "token": token[1] # in previous version, "token": token - now need token[1]
    })    


# Login API
class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data

    token = AuthToken.objects.create(user)
    return Response({
      "user": UserSerializer(
        user, context=self.get_serializer_context()).data,
        "token": token[1] 
    })    


# Get User API
# E.g. in Postman, GET request to http://127.0.0.1:8000/api/auth/user
# - add header entry with KEY=" Authorization ", VALUE=" Token <active_token_for_specific_user> " (plus the usual Content-Type, application/json)
#   - token is loaded from the browser's localStorage if available there upon entering the website
#   - no endpoint set up for doing this in a browser using e.g. query parameter, that could of course be added as well
class UserAPI(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
    # permissions.AllowAny, 
  ]
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user



class ProfileAPI(generics.RetrieveAPIView): # RetrieveAPIView: Used for read-only endpoints to represent a single model instance. (ListAPIView for a collection of...)
  permission_classes = [
    # permissions.IsAuthenticated,
    permissions.AllowAny, 
  ]
  serializer_class = ProfileSerializer
  queryset = Profile.objects.all()

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs) 

