from django.contrib import admin
from .models import Post
from django.contrib.auth.models import Permission, User


admin.site.register(Post)
admin.site.register(Permission)

