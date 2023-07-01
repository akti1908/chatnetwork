from django.db import models
from myusers.models import My_user


class Chat(models.Model):
    sender = models.ForeignKey(My_user, related_name='sent_chats', on_delete=models.CASCADE)
    taker = models.ForeignKey(My_user, related_name='received_chats', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
