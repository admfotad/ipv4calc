from django.conf.urls import include, url 
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from collection import views
from .views import (
ipv4,
)

urlpatterns = [
    url(r'^$',ipv4),
    
        ]