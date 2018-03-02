# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import UserSignUp
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def signup(request):
    if request.method == 'POST':
        form = UserSignUp(request)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('post_list')
        else:
            form = UserSignUp()
    return render(request, 'signup.html', {'form': form})