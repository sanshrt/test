from django.contrib import admin
from .models import Workshop, WorkshopRegister

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'fees')  # Display name, date, and fees
    search_fields = ('name',)  # Enable search by name

@admin.register(WorkshopRegister)
class WorkshopRegisterAdmin(admin.ModelAdmin):
    list_display = ('workshop', 'student', 'registration_date', 'pay')  # Display these fields in admin
    list_filter = ('pay',)  # Filter by payment status
