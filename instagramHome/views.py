from django.shortcuts import render, redirect
from .models import Post,Comment
from .froms import PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    post = Post.objects.all().order_by('-last_modified')

    context={
        'posts' : post,
    }
    return render(request, 'instagramHome/home.html',context)


def about(request):
    return render(request, 'instagramHome/about.html', {'title': 'About'})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            post_name = form.cleaned_data.get('image_name')
            messages.success(request, f'Your post has been created for{post_name}!')
            return redirect('instagramHome-home')
    else:
        form = PostForm()
    
    context = {
        'form' : form
    }

    return render(request, 'instagramHome/newPost.html',context, {'title':'New Post'})

