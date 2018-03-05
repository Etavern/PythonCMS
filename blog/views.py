# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponseRedirect
from django.utils import timezone
from .forms import UserSignUp, PostForm, PasswordResetForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import Group
from django.conf import settings
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    print(request.user.groups)
    print(request.user.groups.filter(name='New').count())
    if request.user.groups.filter(name='New').count() is 0:
        notnew = 'yes'
        print(notnew)
    else:
        notnew = 'no'
    return render(request, 'blog/post_list.html', {'posts': posts, 'notnew': notnew})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.groups.filter(name='New').count() is 0:
        notnew = 'yes'
        print(notnew)
    else:
        notnew = 'no'
    return render(request, 'blog/post_detail.html', {'post': post, 'notnew': notnew})


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


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, 'You have successfully deleted the post')
    return redirect('post_list')


def reset_password(request):
    print("SOMEONE SHOULD HAVE USED A F$%kING PASSWORD MANAGER")
    return redirect('post_list')


def account(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Success!')
                return redirect('account')
            else:
                messages.error(request, 'Error!')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'blog/account.html', {'form': form})
    else:
        return HttpResponseRedirect('/login')


def signup(request):
    if request.method == 'POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            group = Group.objects.get(name='New')
            user.groups.add(group)
            login(request, user)
            print("A NEW VICTIM HAS BEEN ENTERED")
            return redirect('post_list')
    else:
        form = UserSignUp()
    return render(request, 'blog/signup.html', {'form': form})
