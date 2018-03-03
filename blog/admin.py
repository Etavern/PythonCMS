from django.contrib import admin
from .models import Post
from django.contrib.auth.models import Permission


admin.site.register(Permission)
admin.site.register(Post)
