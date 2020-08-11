from rest_framework import serializers
from .models import Paper, Comment #, UserSavedPaper

from accounts.serializers import UserSerializer # cannot also import serializers from here in accounts.serializers, circular imports

"""
Serializers - https://www.django-rest-framework.org/api-guide/serializers/
- Serializer relations - https://www.django-rest-framework.org/api-guide/relations/
  - alternatively use the "lower level" Serializer instead of ModelSerializer for customizations
"""

# Paper Serializer
class PaperSerializer(serializers.ModelSerializer):
  class Meta:
    model = Paper
    fields = '__all__'


# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'


# Comment Serializer with related data about the user who wrote the comment, to e.g. be able to print out username, show profile picture
class CommentDetailsSerializer(serializers.ModelSerializer):
  user_data = serializers.SerializerMethodField() # -> define a method named get_<field_name> - https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
  
  class Meta:
    model = Comment
    fields = ('id', 'text', 'time', 'user_data') # id "necessary" e.g. for setting key property of div element

  def get_user_data(self, obj):
    user = UserSerializer(obj.profile.user).data
    return user


# - TO DO: Add functionality for logged in user to save/organize favorite papers!
# class UserSavedPaperSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = UserSavedPaper
#     fields = '__all__'