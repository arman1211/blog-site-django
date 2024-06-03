from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from author.forms import RegisterUser,UpdateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post.models import Post



def signup(request):
    if request.method == 'POST':
        register_form = RegisterUser(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Acount created succesfully')
            return redirect('login')
    else:
        register_form = RegisterUser()
        
    
    return render(request, 'register.html', {'form': register_form, 'type': 'Register'})  

def userlogin(request):
    if request.method == 'POST':
        login_form =  AuthenticationForm(request,request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                login(request,user)
                messages.success(request,'Login succesfull')
                return redirect('home')
            else:
                messages.warning(request,'Something went wrong')
                return redirect('register')
    else:
        login_form = AuthenticationForm()

    return render(request,'register.html',{'form': login_form, 'type': 'Login'})

def userlogout(request):
    logout(request)
    return redirect('login')


@login_required
def profie_update(request):
    if request.method == 'POST':
    
        update_form = UpdateUserForm(request.POST,instance = request.user)
        if update_form.is_valid():
            update_form.save()
            messages.success(request,'Acount updated succesfully')
            return redirect('profile')
    else:
        update_form = UpdateUserForm(instance = request.user)
    return render(request,'editprofile.html',{'form': update_form})

@login_required
def change_pass(request):
    if request.method == 'POST':
    
        update_form = PasswordChangeForm(request.user,data = request.POST)
        if update_form.is_valid():
            update_form.save()
            messages.success(request,'Password changed succesfully')
            update_session_auth_hash(request, update_form.user)
            return redirect('profile')
            
    else:
        update_form = PasswordChangeForm(user = request.user)
    return render(request,'passchange.html',{'form': update_form})



def userprofile(request):
    posts = Post.objects.filter(author = request.user)
    return render(request,'profile.html',{'posts': posts})