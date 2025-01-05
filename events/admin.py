from django.contrib import admin
from .models import Event, EventRegistration

class EventRegistrationInline(admin.TabularInline):
    model = EventRegistration
    extra = 0

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'total_registrations')
    search_fields = ('name',)
    inlines = [EventRegistrationInline]

    def total_registrations(self, obj):
        return EventRegistration.objects.filter(event=obj).count()
    total_registrations.short_description = 'Total Registrations'

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'student', 'registration_date')  # Ensure registration_date is included
    list_filter = ('event',)
    search_fields = ('student__username', 'event__name')
    date_hierarchy = 'registration_date'  # Filter by the new field
