from django.shortcuts import render
from post.models import Post

def home(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'home.html',{'posts': posts})