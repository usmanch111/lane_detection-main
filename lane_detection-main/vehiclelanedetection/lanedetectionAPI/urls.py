from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('findlane/', Findlane.as_view(), name='findlane')
]