from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

"""
Using the django shell:
$ python manage.py shell

from django.contrib.auth.models import User
from accounts.models import Profile
from papers.models import Paper, Comment, Rating, UserSavedPaper

users = User.objects.all()
profiles = Profile.objects.all()
papers = Paper.objects.all()
comments = Comment.objects.all()
ratings = Rating.objects.all()
usps = UserSavedPaper.objects.all()

comments.create(text='this is an awesome paper!', profile=profiles[0], paper=papers[0])
"""

# Reversing migrations
# https://docs.djangoproject.com/en/3.0/topics/migrations/#reversing-migrations
# - Ex) $ python manage.py migrate papers zero   <- reverses all migrations for app "papers", see all migrations with "$ python manage.py showmigrations"
#   -> python manage.py makemigrations -> python manage.py migrate


# https://docs.djangoproject.com/en/3.0/ref/models/fields/
class Paper(models.Model):
  title = models.CharField(max_length=200) # About data storage space when specifying a max_length: https://stackoverflow.com/questions/30663791/do-setting-the-max-length-to-a-very-large-value-consume-extra-space
  authors = models.CharField(max_length=200)
  abstract = models.CharField(max_length=2000, blank=True)
  journal = models.CharField(max_length=80, blank=True) 
  date_published = models.DateField(blank=True) # https://www.django-rest-framework.org/api-guide/fields/#datefield
  doi = models.CharField(max_length=32, blank=True)
  pdflink = models.CharField(max_length=80, blank=True)
  avg_rating = models.FloatField(default=0)
  num_ratings = models.PositiveIntegerField(default=0)

  # Useful example for many-to-many in django: https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/
  # - TO DO: Get rid of these fields below in the Paper model? The Comment/Rating/UserSavedPaper tables can exist without them being here!?
  commented_by_users = models.ManyToManyField(
    'accounts.Profile',
    related_name='comments_made',
    through='Comment',
    blank=True
  )

  rated_by_users = models.ManyToManyField(
    'accounts.Profile',
    related_name='ratings_given',
    through='Rating',
    blank=True
  )
  
  saved_by_users = models.ManyToManyField(
    'accounts.Profile',
    related_name="papers_saved",
    through='UserSavedPaper',
    blank=True
  )

  def __str__(self):
    return self.title


# Custom "through" models: https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ManyToManyField.through_fields
class Comment(models.Model):
  text = models.CharField(max_length=500)
  #rating = models.PositiveIntegerField(blank=True) # should rating be given simultaneously with posting a comment?
  time = models.DateTimeField(default=timezone.now) # - TO DO: Look into and decide format for the timestamping
  profile = models.ForeignKey('accounts.Profile', related_name='comments', on_delete=models.CASCADE)
  paper = models.ForeignKey('Paper', related_name='comments', on_delete=models.CASCADE)

  def __str__(self):
    return self.text


# No support for composite primary key, e.g. (profile_id, paper_id) in django? https://stackoverflow.com/questions/15440593/tell-djangos-model-to-use-as-primary-key-a-set-of-foreign-keys
# - https://code.djangoproject.com/wiki/MultipleColumnPrimaryKeys
# - possible to enforce it using SQL commands, using something other than the Django ORM, e.g. SQLAlchemy)
# - there are validators that can be used with a Serializer to enforce "unique together" - https://www.django-rest-framework.org/api-guide/validators/#uniquetogethervalidator
class Rating(models.Model):
  rating = models.PositiveIntegerField()
  profile = models.ForeignKey('accounts.Profile', related_name='ratings', on_delete=models.CASCADE)
  paper = models.ForeignKey('Paper', related_name='ratings', on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.profile.user.username} gave {self.paper.title} a rating of {self.rating}"


# 
class UserSavedPaper(models.Model): 
  profile = models.ForeignKey('accounts.Profile', related_name='saved_papers', on_delete=models.CASCADE)
  paper = models.ForeignKey('Paper', related_name='saved_papers', on_delete=models.CASCADE)
  comment = models.CharField(max_length=500, blank=True)

  def __str__(self):
    return f"user {self.profile.user.username} saved paper {self.paper.title} - comment: {self.comment}"
