from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blog.models import BlogPost, PostComment
from django.forms import Textarea, TextInput

class BlogPostForm (ModelForm):
    class Meta:
        model = BlogPost
        fields = ("title", "body_text")
        widgets = {
                'title': TextInput(attrs={'class': "title-input", "placeholder":"Title"}),
                'body_text': Textarea(attrs={'class': "editable medium-editor-textarea", "cols":1, "rows": 1}),
            }
