from rest_framework import serializers

from .models import Post


# This serializer converts Post objects into JSON data.
class PostSerializer(serializers.ModelSerializer):

    class Meta:

        # Tell DRF which model we are working with.
        model = Post

        # These fields will be included in the API response.
        fields = [
            "id",
            "title",
            "author",
            "content",
            "created_at",
        ]