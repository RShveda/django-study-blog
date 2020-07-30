from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView)
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from blog.models import BlogPost, PostComment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render
from django.forms import Textarea
from blog.forms import BlogPostForm, PostCommentForm


# Create your views here.
# @login_required
def about(request):
    return render(request, "about.html")

@login_required
def publish_post(request, **kwargs):
    id = kwargs["pk"]
    post = BlogPost.objects.get(id=id)
    post.publish()
    post.save()
    return render (request, "blogpost_publish.html", context={"id":id})


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = "/"

# Post views

class PostListView(ListView):
    model = BlogPost

class MyPostsListView(ListView):
    model = BlogPost
    template_name = 'myposts_list.html'

    def get_queryset(self):
        self.author = get_object_or_404(User, username = self.request.user.username)
        return BlogPost.objects.filter(author=self.author)

class PostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = BlogPost

class PostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm

class PostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:post_list')


# Comment views
class CommentCreateView(CreateView):
    model = PostComment
    form_class = PostCommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(BlogPost, id=self.kwargs['post'])
        return super().form_valid(form)

    def get_success_url(self):
        success_url = reverse_lazy('blog:post_details', args = [self.object.post.pk])
        return success_url

class CommentUpdateView(UpdateView):
    model = PostComment
    form_class = PostCommentForm

    def get_success_url(self):
        success_url = reverse_lazy('blog:post_details', args = [self.object.post.pk])
        return success_url

class CommentDeleteView(DeleteView):
    model = PostComment
    def get_success_url(self):
        success_url = reverse_lazy('blog:post_details', args = [self.object.post.pk])
        return success_url
