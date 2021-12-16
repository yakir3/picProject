from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.OneToOneField(User, max_length=20, on_delete=models.CASCADE)
    password = models.CharField(max_length=30)
    token = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"username {self.username}"