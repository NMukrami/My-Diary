
from django.db import models
from django.contrib.auth.models import User

class Diary(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Profile(models.Model):
    profile_picture =models.ImageField(null=True, blank=True, default="default-profile-pic.jpg")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)