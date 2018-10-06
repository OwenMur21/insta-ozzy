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

        
        def save_img(self):
                self.save()

        def del_img(self):
                self.delete()

        @classmethod
        def get_images(cls):
                images = Image.objects.all()
                return images

        @classmethod
        def get_image_by_id(cls, profile):
                image = Image.objects.get(profile_id=profile)
                return image


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
         
        def save_comm(self):
                self.save()

        def del_comm(self):
                self.delete()

        @classmethod
        def get_comments_by_image_id(cls, image):
                comments = Comments.objects.get(image_id=image)
                return comments




 




