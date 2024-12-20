from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paymentAmount = models.IntegerField(null=True, blank=True)
    transactionId = models.CharField(max_length=250, default='')
    transactionDate = models.DateTimeField()
    hasRegistered = models.BooleanField(default=False)

