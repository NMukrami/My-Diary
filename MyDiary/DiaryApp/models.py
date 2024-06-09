from django.db import models
from django.contrib.auth.models import User
import os

class Diary(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)    
    profile_picture = models.ImageField(null=True, blank=True, default="Default.jpg")

    # Override the save method to handle old image deletion   
    def save(self, *args, **kwargs):
        try:
            # Retrieve the old instance of the profile
            old_instance = Profile.objects.get(pk=self.pk)

            # Check if the profile picture has changed
            if old_instance.profile_picture and old_instance.profile_picture != self.profile_picture:
                
                # Remove the old profile picture file from the filesystem
                if os.path.isfile(old_instance.profile_picture.path):
                    os.remove(old_instance.profile_picture.path)

        except Profile.DoesNotExist:
             # If the profile does not exist, this is the first save, so no action is needed
            pass

        # Call the original save method to save the new profile picture
        super().save(*args, **kwargs)

