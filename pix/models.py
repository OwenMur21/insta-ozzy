from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField

class Profile(models.Model):
        """
        Class that contains profile details
        """
        bio = HTMLField()
        dp = ImageField(blank = True)
        user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)


        def __str__(self):
                return self.bio
 




