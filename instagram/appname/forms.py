from django import forms
from .models import Post, CustomUser, Comment, Hashtag

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

# from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'location','content','image','hashtag_field']

class SigninForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','password']
        help_texts = {
            'username': None,
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','password','nickname','phone_number','profile_image']
        help_texts = {
            'username': None,
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        ordering = ['-timestamp']
        fields = ['name']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name','last_name']



