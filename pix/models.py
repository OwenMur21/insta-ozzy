from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    """
    Class that contains details of a user's profile
    """
    pic = models.ImageField(upload_to = 'images/')
    bio = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
            return self.name

    def save_profile(self):
            self.save()

    def del_profile(self):
            self.delete()

class Image(models.Model):
    """
    Class that contains details of an image
    """
    image = models.ImageField(upload_to= 'images/')

