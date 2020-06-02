from django.shortcuts import render, redirect
from .models import Post,Comment

# Create your views here.

def home(request):
    post = Post.objects.all().order_by('-last_modified')

    context={
        'posts' : post,
    }
    return render(request, 'instagramHome/home.html',context)


def about(request):
    return render(request, 'instagramHome/about.html', {'title': 'About'})

