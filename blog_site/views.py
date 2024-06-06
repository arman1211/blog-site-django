from django.shortcuts import render
from post.models import Post
from catagory.models import Catagory
from django.views.generic import DetailView


def home(request,catagory_slug = None):
    posts = Post.objects.all()
    if catagory_slug is not None:
        catagory = Catagory.objects.get(slug = catagory_slug)
        posts = Post.objects.filter(catagory = catagory)
    catagory = Catagory.objects.all()
    return render(request, 'home.html',{'posts': posts,'catagory': catagory})

class DetailPostView(DetailView):
    model = Post
    template_name = 'detailpost.html'
    