from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

from rest_framework.permissions import IsAuthenticated

def home(request):
    return HttpResponse(
        "Hello world my django is working"
    )


class PostListCreateAPIView(generics.ListCreateAPIView):

    queryset = Post.objects.all()

    serializer_class = PostSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        "author",
    ]

    search_fields = [
        "title",
        "content",
        "author",
    ]

    ordering_fields = [
        "title",
        "created_at",
    ]

    ordering = [
        "-created_at",
    ]


class PostDetailAPIView(APIView):

    def get(self, request, post_id):

        post = get_object_or_404(
            Post,
            id=post_id
        )

        serializer = PostSerializer(post)

        return Response(serializer.data)




class ProtectedAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response({
            "message": "You are authenticated!",
            "username": request.user.username
        })