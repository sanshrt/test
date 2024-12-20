from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    college_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email_id = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
