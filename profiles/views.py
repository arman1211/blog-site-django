from django.shortcuts import render,redirect
from profiles.forms import ProfileForm

# Create your views here.

def profiles(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profiles')
    else:
        profile_form = ProfileForm()
    return render(request,'profile.html',{'form': profile_form})
