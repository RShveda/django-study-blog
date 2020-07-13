"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('posts/new', views.PostCreateView.as_view(), name='post_create'),
    path('posts/edit/<pk>', views.PostUpdateView.as_view(), name='post_edit'),
    path('posts/delete/<pk>', views.PostDeleteView.as_view(), name='post_delete'),
    path('posts/<pk>', views.PostDetailView.as_view(), name='post_details'),
    path('comments/new/<int:post>', views.CommentCreateView.as_view(), name='comment_create'),
    path('comments/edit/<pk>', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/delete/<pk>', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('about/', views.about, name='about'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name = "login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name = "logout"),
    path('accounts/signup/', views.UserCreateView.as_view(), name = "signup"),
]
