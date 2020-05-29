from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return render(request, 'instagramUsers/register.html', {'form':form})
    else:
        form = UserRegisterForm()
    return render(request, 'instagramUsers/register.html', {'form':form})