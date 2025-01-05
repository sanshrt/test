from django.contrib import admin
from .models import Workshop, WorkshopRegistration

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'price')


@admin.register(WorkshopRegistration)
class WorkshopRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'workshop', 'payment_status')
    list_filter = ('payment_status',)
    search_fields = ('user__username', 'workshop__name')
