from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Thread(models.Model):
    participants = models.ManyToManyField(User, related_name='threads')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Thread {self.id}'


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message {self.id} in Thread {self.thread.id}'
