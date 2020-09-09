from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, null= True, blank = True, on_delete = models.CASCADE)
    name = models.CharField(max_length=200, null = True)
    UserProfile_pic = models.ImageField(default = "images/default-user-pic.jpg",upload_to="user_images",  null=True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.name
