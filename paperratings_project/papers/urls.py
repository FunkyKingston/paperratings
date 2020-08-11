from rest_framework import routers
from django.urls import path, include
from .api import PaperViewSet


from .api import CommentListCreate, CommentRetrieveUpdateDestroy
from .api import CommentListByPaper
from .api import CommentDetailsRetrieve, CommentDetailsList


router = routers.DefaultRouter() # use router to set up urls for viewsets, here the PaperViewSet
router.register('papers', PaperViewSet) # viewset urls include (necessary to use) trailing '/'


# these urlpatterns are included in the main urls file under /api/..
urlpatterns = [ 
    path('', include(router.urls)),
    path('comments/', CommentListCreate.as_view()), # class CommentListCreate(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroy.as_view()), # http://127.0.0.1:8000/api/comments/3/

    path('commentlistbypaper', CommentListByPaper.as_view()), # e.g. http://127.0.0.1:8000/api/commentlistbypaper?paper_id=1
    
    path('commentdetails/', CommentDetailsList.as_view()), 
    path('commentdetails/<int:pk>/', CommentDetailsRetrieve.as_view()), 

    # path('commentapiview', CommentAPIView.as_view()),
]

"""
Examples:
POST http://127.0.0.1:8000/api/papers/
Headers:
KEY Content-Type VALUE application/json
Body (raw - JSON):
{
	"title": "Online Measurements of Alkali Metals during Start-up and Operation of an Industrial-Scale Biomass Gasification Plant", 
	"authors": "Dan Gall, Mohit Pushp, Anton Larsson, Kent Davidsson, Jan B. C. Pettersson",
	"abstract": "Alkali metal compounds may have positive influences on biomass gasification by affecting char reactivity and tar reforming but may also disturb the process by formation of deposits and agglomerates. We herein present results from online measurements of alkali compounds and particle concentrations in a dual fluidized bed gasifier with an input of 32 MWth. A surface ionization detector was used to measure alkali concentrations in the product gas, and aerosol particle measurement techniques were employed to study concentrations and properties of condensable components in the gas. Measurements were performed during start-up and steady-state operation of the gasifier. The alkali concentration increased to approximately 200 mg m–3 when fuel was fed to the gasifier and continued to rise during activation of the olivine bed by addition of potassium carbonate, while the alkali concentration was in the range from 20 to 60 mg m–3 during steady-state operation. Addition of fresh bed material and recirculated ash had noticeable effects on the observed alkali concentrations, and K2CO3 additions to improve tar chemistry resulted in increased levels of alkali in the product gas. Addition of elemental sulfur led to reduced concentrations of CH4 and heavy tars, while no clear influence on the alkali concentration was observed. The study shows that alkali concentrations are high in the product gas, which has implications for the fluidized bed process, tar chemistry, and operation of downstream components including coolers, filters, and catalytically active materials used for product gas reforming.",
	"journal": "Energy Fuels, American Chemical Society",
	"date_published": "2015-06-02",
	"doi": "10.1021/acs.energyfuels.7b03135",
	"pdflink": ""
}

POST http://127.0.0.1:8000/api/comments/
Headers:
KEY Content-Type VALUE application/json
Body (raw - JSON):
{
    "text": "Test from Postman",
    "profile": 1,
    "paper": 1
}

-> Response
{
    "id": 2,
    "text": "Test from Postman",
    "time": "2020-07-08T20:48:46.594255Z",
    "profile": 1,
    "paper": 1
}

...

"""