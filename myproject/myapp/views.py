from django.shortcuts import render
from django.shortcuts import get_object_or_404

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




class PostDetailAPIView(APIView):
    """
    API view for retrieving one blog post.
    """

    def get(self, request, post_id):
        # Find the post using the ID supplied in the URL.
        post = get_object_or_404(
            Post,
            id=post_id
        )

        # We are serializing ONE object,
        # so we do not use many=True.
        serializer = PostSerializer(post)

        # Return the post as JSON.
        return Response(serializer.data)
