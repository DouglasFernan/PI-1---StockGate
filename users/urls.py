from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("index/", views.index, name="index"),
]
