from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Avi
from django.core.files.images import get_image_dimensions


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class UserSignUp(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='This field is more mandatory than Crypto.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserAviForm(forms.ModelForm):
    class Meta:
        model = Avi
        fields = ('avatar', )






