from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("blog/", views.blog, name="blog"),
]
