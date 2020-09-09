from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    caption_text = models.CharField(max_length=500)
    blog_text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="blog_images", blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption_text[:30]
