from django.urls import path,include
from profiles.views import profiles

urlpatterns = [
    path('',profiles, name='profiles')
]
