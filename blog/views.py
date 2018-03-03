# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Post, Avi
from django.utils import timezone
from .forms import UserSignUp, PostForm, UserAviForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.conf import settings
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def reset_password(request):
    print("SOMEONE SHOULD HAVE USED A F$%kING PASSWORD MANAGER")
    return redirect('post_list')


def account(request):
    avi = get_object_or_404(Avi, user=request.user)
    if request.method == 'POST':
        form = UserAviForm(request.POST)
        if form.is_valid:
            print(valid)
    else:
        form = UserAviForm()

    return render(request, 'blog/account.html', {'form': form, 'avi': avi.avatar.url, 'root': settings.MEDIA_ROOT})


def signup(request):
    if request.method == 'POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        form = UserSignUp()
    return render(request, 'blog/signup.html', {'form': form, 'avi': Avi})
