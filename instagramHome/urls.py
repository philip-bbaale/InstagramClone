from django.urls import path
from . import views

urlpatterns = [
    path('Phome', views.home, name='instagramHome-home'),
    path('Pabout/', views.about, name='instagramHome-about'),
]