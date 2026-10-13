
import pytest
from rest_framework.test import APIClient
from myapp.models import Post


@pytest.mark.django_db
def test_post_list_api():

    # Create a blog post
    Post.objects.create(
        title="Testing Django API",
        author="Leonard",
        content="Learning automated testing"
    )

    # Create an API client
    client = APIClient()

    # Send a GET request to the API
    response = client.get("/api/posts/")

    # Check the response
    assert response.status_code == 200

    # Check that one post was returned
    assert len(response.data) == 1
