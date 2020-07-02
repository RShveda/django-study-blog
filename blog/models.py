from django.db import models
# Create your models here.

class BlogPost (models.Model):
    title = models.CharField(max_length = 128)
    body_text = models.CharField(max_length = 256)

class PostComment (models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name = "comments")
    comment_text = models.CharField(max_length = 128)
