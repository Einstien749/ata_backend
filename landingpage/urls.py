# Create your views here.

from django.urls import path, include

from .views import *

urlpatterns = [
    path('', portfolioview),
]
