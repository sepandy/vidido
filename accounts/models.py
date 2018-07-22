from django.contrib.auth.models import User
from django.db import models
# from django.contrib.auth import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse_lazy
# from django.db import models as dbModel
# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    profile_photo = models.ImageField(verbose_name="photo", null=True, blank=True,upload_to='avatars/',default='../static/facebook-avatar.jpg')
    birthday = models.DateField(null=True)
    bio = models.TextField(max_length=500 , null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'male'), ('female' , 'female'), ('other', 'other') ,('alien', 'alien')])
    friends = models.ManyToManyField('self', db_index=True, related_name='friends',)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender = User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    instance.profile.save()