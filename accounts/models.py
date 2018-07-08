from django.contrib.auth.models import User
from django.db import models
# from django.contrib.auth import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse_lazy
# from django.db import models as dbModel
from posts.models import Post
# Create your models here.


# class User(models.User, models.PermissionsMixin, dbModel.Model):
#     friends = dbModel.ManyToManyField(Post, related_name='Friends', db_index=True)
#
#     def __str__(self):
#         return "@{}".format(self.username)

class Profile(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    birthday = models.DateField(null=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'male'), ('female' , 'female'), ('other', 'other') ,('alien', 'alien')])
    friends = models.ManyToManyField('self', db_index=True, related_name='friends')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender = User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    instance.profile.save()