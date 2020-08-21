from django.contrib import admin
from django.urls import path, include
# from django.urls import re_path

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    path('api/', include('papers.urls')), # note the trailing '/'
    path('api/', include('accounts.urls')),    
] # + [url('', TemplateView.as_view(template_name="index.html"))]


if settings.DEBUG: # allows to serve (user-uploaded) media files during development/debug mode only
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# The React URLs need to be added last, otherwise the django URLs are overridden
urlpatterns += [url('', TemplateView.as_view(template_name="index.html"))]