from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI, ProfileAPI
from knox import views as knox_views



urlpatterns = [
  path('auth', include('knox.urls')),
  path('auth/register', RegisterAPI.as_view()),
  path('auth/login', LoginAPI.as_view()),
  path('auth/user', UserAPI.as_view()), # get request to http://127.0.0.1:8000/api/auth/user - no id in the path, user is identified by included header entry: KEY 'Authenticate', VALUE "Token <active token>"
  path('auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'), # the knox logout is gonna invalidate the token (that's created during login)

  path('auth/profile/<int:pk>/', ProfileAPI.as_view()), # http://127.0.0.1:8000/api/auth/profile/1/


]

"""
Examples)
POST http://127.0.0.1:8000/api/auth/register
Headers:
KEY Content-Type VALUE application/json
Body (raw - JSON):
{
    "username": "MamaJamaica",
    "email": "mama@gmail.com",
    "password": "123456" 
}

GET http://127.0.0.1:8000/api/auth/user - no need to add user id, user is identified by the passed along token in the header
Headers:
KEY Content-Type VALUE application/json
KEY Authorization VALUE Token <active_token>


GET http://127.0.0.1:8000/api/auth/profile/1/
Headers:
KEY Content-Type VALUE application/json

"""

