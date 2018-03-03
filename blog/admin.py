from django.contrib import admin
from .models import Post, Avi
from django.contrib.auth.models import Permission, User


admin.site.register(Post)
admin.site.register(Permission)
admin.site.register(Avi)
