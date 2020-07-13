from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView)
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from blog.models import BlogPost, PostComment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
# @login_required
def about(request):
    return render(request, "about.html")

class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = "/"

# Post views

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


# Comment views
class CommentCreateView(CreateView):
    model = PostComment
    fields = ["comment_text"]

    def form_valid(self, form):
        # TODO add Post relation here
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(BlogPost, id=self.kwargs['post'])
        return super().form_valid(form)

    def get_success_url(self):
        success_url = reverse_lazy('blog:post_details', args = [self.object.post.pk])
        return success_url

class CommentUpdateView(UpdateView):
    model = PostComment
    fields = ["comment_text"]

    def get_success_url(self):
        success_url = reverse_lazy('blog:post_details', args = [self.object.post.pk])
        return success_url

class CommentDeleteView(DeleteView):
    model = PostComment
    # success_url = reverse_lazy('blog:post_details', args = [])
    def get_success_url(self):
        success_url = reverse_lazy('blog:post_details', args = [self.object.post.pk])
        return success_url
