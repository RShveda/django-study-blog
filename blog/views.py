from django.shortcuts import render
from django.views.generic import (ListView)
from django.views.generic.edit import (CreateView)
from blog.models import BlogPost, PostComment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def about(request):
    return render(request, "about.html")

class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = "/"

class PostListView(ListView):
    model = BlogPost
