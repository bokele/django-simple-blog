from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DetailView,  ListView, TemplateView, DeleteView
from app_blog.models import Blog, BlogComment, Likes
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from app_blog.forms import CommentForm




class  BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'app_blog/blog_list.html'


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    already_liked = Likes.objects.filter(blog=blog, user=request.user)
    comment_form = CommentForm()
    if already_liked:
        liked = True
    else:
        liked = False


    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog= blog
            comment.save()
            return HttpResponseRedirect(reverse('app_blog:detail_blog', kwargs={'slug':slug}))

    return render(request, 'app_blog/blog_detail.html', context={ 'blog_detail':blog, 'comment_form':comment_form, 'liked':liked })

class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    fields =['blog_title', 'blog_content', 'blog_image']
    template_name = 'app_blog/create_blog.html'

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

@login_required
def liked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_like = Likes.objects.filter(blog=blog, user=user)
    if not already_like:
        like_post = Likes(blog=blog, user=user)
        like_post.save()
    return HttpResponseRedirect(reverse('app_blog:detail_blog', kwargs={'slug':blog.slug}))

@login_required
def unliked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_like = Likes.objects.filter(blog=blog, user=user)
    already_like.delete()
    return HttpResponseRedirect(reverse('app_blog:detail_blog', kwargs={'slug':blog.slug}))

class MyBlogs(LoginRequiredMixin, TemplateView):
    template_name = 'app_blog/my_blog.html'


class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    fields =['blog_title', 'blog_content', 'blog_image']
    template_name = 'app_blog/edit_blog.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('app_blog:detail_blog', kwargs={'slug':self.object.slug})
