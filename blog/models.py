from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class BlogPost (models.Model):
    title = models.CharField(max_length = 128)
    body_text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(null=True, blank = True)

    def publish(self):
        self.published_at = timezone.now()
        return self.published_at

    def get_absolute_url(self):
        return reverse('blog:blogpost', args=[str(self.id)])

    def __str__(self):
        return self.title


class PostComment (models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name = "comments")
    comment_text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('blog:comment', args=[str(self.id)])

    def __str__(self):
        return self.text
