from django.db import models
from django.contrib.auth.models import User



class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    UserProfile_pic = models.ImageField(default = "images/default-user-pic.jpg",upload_to="user_images",  null=True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
