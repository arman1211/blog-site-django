from django.shortcuts import render
from post.models import Post
from catagory.models import Catagory

def home(request,catagory_slug = None):
    posts = Post.objects.all()
    if catagory_slug is not None:
        catagory = Catagory.objects.get(slug = catagory_slug)
        posts = Post.objects.filter(catagory = catagory)
    catagory = Catagory.objects.all()
    return render(request, 'home.html',{'posts': posts,'catagory': catagory})