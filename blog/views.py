from django.shortcuts import render
from django.views.generic import (ListView)
from blog.models import BlogPost, PostComment
# Create your views here.

def about(request):
    return render(request, "about.html")

class PostListView(ListView):
    model = BlogPost
