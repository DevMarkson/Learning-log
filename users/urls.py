"""Defines URL patterns for Users"""

from django.urls import path, include
from . import views

app_name = "users"
urlpatterns = [
    # incluude default authentication urls
    path("", include("django.contrib.auth.urls")),
    # Registration page
    path("register/", views.register, name="register"),
]