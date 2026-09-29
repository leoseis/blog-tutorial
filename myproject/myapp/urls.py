from django.urls import path

from . import views


urlpatterns = [

    # Normal Django page
    path(  "",views.home,   name="home"),

    # Blog API
    path("api/posts/", views.PostListAPIView.as_view(), name="api_posts")]