from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Workshop(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=500)
    date = models.DateField()
    urls = models.CharField(max_length=500)
    fees = models.IntegerField()

    def __str__(self):
        return self.name


class WorkshopRegister(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    pay = models.BooleanField(default=False)  # Default value is False

    def __str__(self):
        return f"{self.student.username} - {self.workshop.name} - {'Paid' if self.pay else 'Pending'}"