from django.urls import path

from . import views


urlpatterns = [
    # Normal Django page
    path("", views.home, name="home"),
    # getting an id post
    path("api/posts/<int:post_id>/", views.PostDetailAPIView.as_view(), name="api_post_detail"),
    # Blog API getting all
    path("api/posts/", views.PostListAPIView.as_view(), name="api_posts"),
]


