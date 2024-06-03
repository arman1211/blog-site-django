from django.shortcuts import render,redirect
from post.forms import PostForm
from post.models import Post

# Create your views here.

def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save(commit=False)
            post_form.instance.author = request.user
            post_form.save()
            return redirect('home')
    else:
        post_form = PostForm()
        
    
    return render(request, 'post.html', {'form': post_form})

def edit_post(request,id):
    post = Post.objects.get(pk=id)
    post_form = PostForm(instance=post)
    if request.method == 'POST':
        post_form = PostForm(request.POST ,instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
    
        
    
    return render(request, 'post.html', {'form': post_form})
def delete_post(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')
    