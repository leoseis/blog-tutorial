from django.urls import path

from . import views

urlpatterns = [

    # Normal Django page
    path(
        "",
        views.home,
        name="home"
    ),

    # Blog API
    # GET = list posts
    # POST = create post
    path(
        "api/posts/",
        views.PostListCreateAPIView.as_view(),
        name="api_posts"
    ),

    # Get one post
    path(
        "api/posts/<int:post_id>/",
        views.PostDetailAPIView.as_view(),
        name="api_post_detail"
    ),
]