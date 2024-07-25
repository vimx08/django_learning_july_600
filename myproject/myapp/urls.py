from django.urls import path
from.views import myapp_home

urlpatterns = [
    path("home/",myapp_home)
]

