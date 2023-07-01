from django.db import models
from myusers.models import My_user


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(My_user,on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    description = models.TextField()
    # cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.content



class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')


