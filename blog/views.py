from django.shortcuts import render
from django.views.generic import (ListView, DetailView)
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from blog.models import BlogPost, PostComment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

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

class PostCreateView(CreateView):
    model = BlogPost
    fields = ["title", "body_text"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = BlogPost

class PostUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "body_text"]

class PostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:post_list')
