from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    pic = models.CharField(max_length=500)
    doc = models.CharField(max_length=1000,null=True,blank=True)
    def __str__(self):
        return self.name

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)  # Automatically add the current date/time when created

    def __str__(self):
        return f"{self.student.username} - {self.event.name}"
