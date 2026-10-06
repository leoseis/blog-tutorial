from django.urls import path

from . import views

# JWT imports
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    # Normal Django page
    path(
        "",
        views.home,
        name="home"
    ),

    # Blog API
    # GET  -> get all posts
    # POST -> create a post
    path(
        "api/posts/",
        views.PostListCreateAPIView.as_view(),
        name="api_posts"
    ),

    # Get one blog post
    path(
        "api/posts/<int:post_id>/",
        views.PostDetailAPIView.as_view(),
        name="api_post_detail"
    ),

    # JWT login
    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),

    # Get a new access token
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),

    path(
    "api/protected/",
    views.ProtectedAPIView.as_view(),
    name="protected"
),
]