from django.db import models
from accounts import models as accountsModel
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    text = models.TextField(max_length=300)
    shareDate = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(accountsModel.Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.user.username + ' --- ' + str(self.shareDate)