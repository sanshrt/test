from django.db import models
from django.contrib.auth.models import User

# Event model to represent an event
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name

# EventRegistration model to handle the registration of students for events
class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.username} registered for {self.event.name}'
