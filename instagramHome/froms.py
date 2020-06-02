from django import forms

class PostForm(forms.Form):
    image = forms.ImageField()
    image_name = forms.CharField(label='Image Name')
    image_caption = forms.Textarea(label='Image Caption')

class CommentForm(forms.Form):
    body = forms.Textarea(lable='Type a Comment')
