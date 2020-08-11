from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    path('api/', include('papers.urls')), # note the trailing '/'
    path('api/', include('accounts.urls')),
    url('', TemplateView.as_view(template_name="index.html")),
]
