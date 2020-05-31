from django.shortcuts import render

# Create your views here.

posts = [
    {
        'image':'xxx',
        'image_name':"Coding",
        'image_caption':'Love Treese Life code Eat drink SLEEP',
        'profile':'pip_bbaale',
        'Likes':'200',
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render(request, 'instagramHome/home.html',context)


def about(request):
    return render(request, 'instagramHome/about.html', {'title': 'About'})

