# models.py

from django.db import models
from django.contrib.auth.models import User

class Accommodation(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    
    MEAL_CHOICES = [
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
        ('A', 'All'),
    ]
    
    # User who is adding the accommodation
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')  # Gender field
    hostel_required = models.BooleanField(default=False)  # Checkbox for hostel requirement
    meal_option = models.CharField(max_length=10, choices=MEAL_CHOICES, default=False)  # Meal option field
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the creation timestamp

    def __str__(self):
        return f"Accommodation for {self.user.username}"
