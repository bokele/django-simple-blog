from django import  forms
from app_blog.models import Blog, BlogComment, Likes

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('comment',)
