from django.urls import path
from django.conf.urls import include
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
path("login/", views.login_view, name="login"),
path("", views.home, name="home"),
path('logout/', LogoutView.as_view(), name='logout'),

]