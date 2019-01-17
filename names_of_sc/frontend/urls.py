# Basic Django imports
from django.contrib import admin
from django.urls import path

# Imports for custom code
from frontend.views import MainPage

# All Patterns that could be used in the website
urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('map', MainPage.as_view(), name='map'),
    path('regions', MainPage.as_view(), name='regions'),
    path('counties', MainPage.as_view(), name='counties'),
    path('authors', MainPage.as_view(), name='authors'),
]
