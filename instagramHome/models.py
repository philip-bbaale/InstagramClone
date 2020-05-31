from django.db import models
from instagramUsers.models import Profile

# Create your models here
"""
class Post(models.Model):
    image = models.ImageField(upload_to='post_images')
    image_name = models.CharField(max_length=100)
    image_caption = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    User = models.ForeignKey('Profile', on_delete=models.CASCADE)
    likes = models.IntegerField()

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    """