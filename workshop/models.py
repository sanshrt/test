from django.db import models
from django.contrib.auth.models import User

class Workshop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='workshop_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class WorkshopRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.workshop.name}"
