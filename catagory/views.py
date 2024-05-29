from django.shortcuts import render,redirect
from catagory.forms import CatagoryForm

# Create your views here.

def add_catagory(request):
    if request.method == 'POST':
        catagory_form = CatagoryForm(request.POST)
        if catagory_form.is_valid():
            catagory_form.save()
            return redirect('catagory')
    else:
        catagory_form = CatagoryForm()
        
    
    return render(request, 'catagory.html', {'form': catagory_form})
