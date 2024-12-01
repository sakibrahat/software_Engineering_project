
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields if needed in the future, e.g., profile picture, bio, etc.

    def __str__(self):
        return self.user.username
