
from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView

from blog.models import Post

# Create your views here.
#home page list view
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_post_list'

class DetailPostView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

# class NewPostCreate(CreateView):
#     model = Post
#     template_name = 'new_post.html'