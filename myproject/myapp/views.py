from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


def home(request):
    return HttpResponse(
        "Hello world my django is working"
    )


class PostListCreateAPIView(APIView):

    def get(self, request):
        posts = Post.objects.all()

        serializer = PostSerializer(
            posts,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=201
            )

        return Response(
            serializer.errors,
            status=400
        )


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