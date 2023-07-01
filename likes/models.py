from django.db import models
from myusers.models import My_user
from posts.models import Post


class Like(models.Model):
    author = models.ForeignKey(My_user, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = ('author', 'post')
