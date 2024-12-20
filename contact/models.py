from django.db import models
from django.contrib.auth.models import User  # Assuming the user is linked to the built-in User model

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message from {self.user.username} on {self.timestamp}'
