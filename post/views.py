from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from post.forms import PostForm
from post.models import Post
from django.contrib import messages


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

# class view for add post 

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def edit_post(request,id):
    post = Post.objects.get(pk=id)
    post_form = PostForm(instance=post)
    if request.method == 'POST':
        post_form = PostForm(request.POST ,instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')

    
    return render(request, 'post.html', {'form': post_form})

# class view for delete post

class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def edit(self, request, *args, **kwargs):
        response = super().edit(request, *args, **kwargs)
        messages.success(request, "Post edited successfully!")
        return response
    


def delete_post(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')
    

# class view for delete post 
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, "Post deleted successfully!")
        return response
    
    