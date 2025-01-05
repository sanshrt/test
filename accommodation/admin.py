from django.contrib import admin
from .models import Accommodation

class AccommodationAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'hostel_required', 'meal_option', 'created_at']
    list_filter = ['hostel_required', 'gender', 'meal_option']  # Add filters for better visibility
admin.site.register(Accommodation,AccommodationAdmin)