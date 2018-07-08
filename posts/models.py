from django.db import models
from accounts.models import User
# Create your models here.


class Post(models.Model):
    text = models.TextField(max_length=300)
    shareDate = models.DateTimeField(auto_now=True)
    taggedUsers = models.ManyToManyField(User, related_name='TaggedPeople', db_index=True)