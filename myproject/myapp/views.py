from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


def home(request):
    return HttpResponse("Hello world my django is working")
# Create your views here.



# DRF API view
class PostListAPIView(APIView):

    def get(self, request):

        # Get all blog posts from the database.
        posts = Post.objects.all()

        # Convert the Django objects into JSON-ready data.
        # many=True is required because we have multiple posts.
        serializer = PostSerializer(
            posts,
            many=True
        )

        # Send the serialized data back to the client.
        return Response(serializer.data)