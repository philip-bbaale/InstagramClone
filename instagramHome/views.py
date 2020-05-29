from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'instagramHome/home.html')


def about(request):
    return render(request, 'instagramHome/about.html', {'title': 'About'})

