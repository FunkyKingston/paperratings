from rest_framework import viewsets, permissions, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Paper, Comment #, UserSavedPaper
from .serializers import PaperSerializer, CommentSerializer, CommentDetailsSerializer #, UserSavedPaperSerializer



# PaperViewSet - using a ViewSet provides full CRUD API (Create, Read, Update, Delete) - https://www.django-rest-framework.org/api-guide/viewsets/#viewsets
# - TO DO: for now use AllowAny permission for all /api/papers/ operations, later on this should be read only for non-admins
class PaperViewSet(viewsets.ModelViewSet):
  queryset = Paper.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = PaperSerializer



"""
Notes to self, in the spirit of learning Django:
The Comment API endpoints, defined below, use the GenericAPIView class and various mixin classes (as opposed to the Paper API which subclasses viewsets.ModelViewSet)
- rest_framework.generics.GenericAPIView inherits from the rest_framework.views.APIView class, which in turn inherits from django.views.generics.View

django_rest_framework code:
- serializers.py - https://github.com/encode/django-rest-framework/blob/master/rest_framework/serializers.py
  - ModelSerializer's .create() method "is essentially just: return ExampleModel.objects.create(**validated_data)"
    - class Serializer(BaseSerializer...), class ModelSerializer(Serializer)
- generics.py - https://github.com/encode/django-rest-framework/blob/master/rest_framework/generics.py
  - GenericAPIView inherits from the APIView class from views.py, which e.g. contains the .as_view() method
- mixins.py - https://github.com/encode/django-rest-framework/blob/master/rest_framework/mixins.py
  - add functionality to the GenericAPIView. Example: the RetrieveAPIView class in generics.py subclasses GenericAPIView with class RetrieveModelMixin mixed in
- views.py - https://github.com/encode/django-rest-framework/blob/master/rest_framework/views.py
  - rest_framework's APIView subclasses the View class in https://github.com/django/django/blob/master/django/views/generic/base.py

"""


# base class to the far right (python inheritance goes from right to left), extended by ListModelMixin, CreateModelMixin 
# - order becomes important when there are some conflicts - video on mixins: https://www.youtube.com/watch?v=rMn2wC0PuXw  
class CommentListCreate(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView): 
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()

  # the get()-method is handled by .as_view() when adding this class as an api view - https://www.pythoninsight.com/2018/03/why-do-django-views-need-an-as_view-method/
  def get(self, request, *args, **kwargs): 
    # return Response("howdy!")
    return self.list(request, *args, **kwargs) # list() is defined in ListModelMixin class in mixin.py

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs) # create() from the CreateModelMixin class, calls its method .perform_create() which calls the serializer's save() method (which in turn calls either create() or update() for the serializer)
  

class CommentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView): # other approach compared to CommentListCreate() above, here I directly subclass RetrieveUpdateDestroyAPIView from generics.py, which in turn subclasses GenericAPIView and uses the Retrieve, Update, Destroy mixin classes
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer




# Get all comments for a specific paper, identified by the 'paper_id' 
# - The frontend React app uses this (and other Comment-endpoints) in frontend/src/actions/comments.js
class CommentListByPaper(generics.ListAPIView): # ListAPIView in generics.py, subclasses GenericAPIView and ListModelMixin
  # serializer_class = CommentSerializer
  serializer_class = CommentDetailsSerializer # When changing serializer, adaptations are necessary to actions/comment.js, reducers/comments.js & Comment.js component

  def get_queryset(self): # override the get_queryset() method of GenericAPIView (which is subclassed by ListAPIView)
    queryset = Comment.objects.all()

    # Filtering against url query parameters - https://www.django-rest-framework.org/api-guide/filtering/#filtering-against-query-parameters
    paper_id = self.request.query_params.get('paper_id', None) # parameter names: seems many APIs use underscore (e.g. not camelCase) 
    if paper_id is not None:
      queryset = Comment.objects.filter(paper=paper_id)

    return queryset



class CommentDetailsList(generics.ListAPIView):
  serializer_class = CommentDetailsSerializer
  queryset = Comment.objects.all()


class CommentDetailsRetrieve(generics.RetrieveAPIView):
  serializer_class = CommentDetailsSerializer
  queryset = Comment.objects.all()



# Maybe later: Play around with APIView and View classes directly instead of using generics.GenericAPIView
# ... https://www.django-rest-framework.org/tutorial/3-class-based-views/
# class CommentAPIView(APIView): 
  
#   def get(self, request, format=None):
#     comments = Comment.objects.all()

#     paper_id = self.request.query_params.get('paper_id', None)
#     if paper_id is not None:
#       comments = Comment.objects.filter(paper=paper_id)
      
#     serializer = CommentSerializer(comments, many=True) # TO DO: custom serializer som lägger till profile.picture, profile.user.username istället för endast profile id
#     # print(serializer.data)
#     return Response(serializer.data)
#     # return Response("Hello from CommentAPIView!")



# class UserSavedPaperList(generics.ListAPIView):
#   serializer_class = UserSavedPaperSerializer
#   permission_classes = [
#     permissions.IsAuthenticated,
#   ]

#   def get_queryset(self):
#     queryset = 