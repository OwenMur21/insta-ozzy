from django.contrib.auth.models import User
import datetime as dt
from django.db import models
from tinymce.models import HTMLField


class Profile(models.Model):
        """
        Class that contains profile details
        """
        bio = HTMLField()
        dp = models.ImageField(upload_to = 'images/', blank=True)
        user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

        def __str__(self):
                return self.bio

        def save_profile(self):
                self.save()

        def del_profile(self):
                self.delete()

        @classmethod
        def search_profile(cls, user):
                profile = cls.objects.filter(user__username__icontains=user)
                return profile
       
class Image(models.Model):
        """
        Class that contains image details
        """
        post = models.ImageField(upload_to = 'images/', blank=True)
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



 




