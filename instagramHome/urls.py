from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='instagramHome-home'),
    path('about/', views.about, name='instagramHome-about'),
]