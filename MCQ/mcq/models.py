from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    Identity = (
        ('teacher','teacher'),
        ('student','student'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    identity = models.CharField(max_length=10, choices=Identity, default='')

    def __str__(self):
        return self.user.username + " " + self.identity
