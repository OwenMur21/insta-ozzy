from django.contrib.auth.models import User
import datetime as dt
from django.db import models
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
        """
        Class that contains profile details
        """
        bio = HTMLField()
        dp = models.ImageField(upload_to = 'images/', blank=True)
        user = models.OneToOneField(User, on_delete=models.CASCADE,null="True")

        @receiver(post_save, sender=User)
        def create_user_profile(sender, instance, created, **kwargs):
                if created:
                        Profile.objects.create(user=instance)

        @receiver(post_save, sender=User)
        def save_user_profile(sender, instance, **kwargs):
                instance.profile.save()

        post_save.connect(save_user_profile, sender=User)

        def save_profile(self):
                self.save()

        def del_profile(self):
                self.delete()

        @classmethod
        def search_profile(cls, name):
                profile = cls.objects.filter(user__username__icontains=name)
                return profile

        @classmethod
        def get_by_id(cls, id):
                profile = Profile.objects.get(id = id)
                return profile
       
class Image(models.Model):
        """
        Class that contains image details
        """
        post = models.ImageField(upload_to = 'images/', blank=True)
        caption = HTMLField()
        posted_on = models.DateTimeField(auto_now_add=True)
        profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
        likes = models.ManyToManyField(User, related_name='likes', blank=True)
        user = models.ForeignKey(User, on_delete=models.CASCADE,null="True")
    
        
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
        def get_image_by_id(cls, id):
                image = Image.objects.filter(user_id=id).all()
                return image


class Comments(models.Model):
        """
        Class that contains comments details
        """
        comment = HTMLField()
        posted_on = models.DateTimeField(auto_now=True)
        image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
        user = models.ForeignKey(User, on_delete=models.CASCADE,null="True")

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




