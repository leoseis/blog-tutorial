from django.db import models

# Create your models herefrom django.db import models


class Post(models.Model):
     # The title of the blog post
    title = models.CharField(max_length=200)

    # The person who wrote the post
    author = models.CharField(max_length=100)

    # The main content of the post
    content = models.TextField()

    # Automatically records when the post was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Show the title when viewing the object in Admin
        return self.title
