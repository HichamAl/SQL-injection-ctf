from django.urls import path
from django.conf.urls import include
from . import views
from django.conf import settings

urlpatterns = [
path("", views.sql, name="sql"),
path("home/", views.home, name="home"),
]