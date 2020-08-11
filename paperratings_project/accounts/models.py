from django.db import models
from django.contrib.auth.models import User

"""
Using the django shell:
$ python manage.py shell

from django.contrib.auth.models import User
from accounts.models import Profile

users = User.objects.all()
profiles = Profile.objects.all()

#users.create(username="", ...)
#About the create() method of models.Model: https://docs.djangoproject.com/en/3.0/ref/models/instances/#creating-objects
#profile.create(user=users[0], location="Betelgeuse Five")
profiles[0].user.username

#User.objects.all().delete()
#Profile.objects.all().delete()
"""

class Profile(models.Model):
  user = models.OneToOneField(User, related_name='profile', primary_key=True, on_delete=models.CASCADE) # https://stackoverflow.com/questions/26188997/django-model-onetoonefield-without-creating-additional-id-database-column
  # user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
  image = models.ImageField(default='default.jpg', upload_to='profile_pics')
  location = models.CharField(max_length=200, blank=True)

  def __str__(self):
    return f"for user {self.user.username}"



