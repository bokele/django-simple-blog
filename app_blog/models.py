from django.db import models
from django.contrib.auth.models import  User

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete =models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=264, verbose_name='Put the title')
    slug=models.SlugField(max_length=264, unique=True)
    blog_content =models.TextField(verbose_name='what is in your mind?')
    blog_image =models.ImageField(upload_to='blog_images', verbose_name='blog image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class  Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.blog_title

class BlogComment(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Likes(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="liked_blog")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
