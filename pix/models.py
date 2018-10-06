from django.contrib.auth.models import User
import datetime as dt
from django.db import models
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField

class Profile(models.Model):
        """
        Class that contains profile details
        """
        bio = HTMLField()
        dp = ImageField(blank = True)
        user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

        def __str__(self):
                return self.bio

class Image(models.Model):
        """
        Class that contains image details
        """
        post = ImageField(blank = True, manual_crop = '1920x1080')
        caption = HTMLField()
        posted_on = models.DateTimeField(auto_now_add=True)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

        def __str__(self):
                return self.caption

        class Meta:
                ordering = ['posted_on']

class Comments(models.Model):
        """
        Class that contains comments details
        """
        comment = HTMLField()
        posted_on = models.DateTimeField(auto_now=True)
        image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
        user = models.ForeignKey(User, on_delete=models.CASCADE)

        def __str__(self):
                return self.comment

        class Meta:
                ordering = ['posted_on']



 




