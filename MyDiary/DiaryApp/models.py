
from django.db import models
from django.contrib.auth.models import User

class Diary(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=400)
    date_post = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)