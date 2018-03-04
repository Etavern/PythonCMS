from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from markdown import markdown
from django.utils.html import mark_safe


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def markdown_message(self):
        return mark_safe(markdown(self.text, safe_mode="escape"))

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

