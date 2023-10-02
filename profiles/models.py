from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Use to store order history for user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)