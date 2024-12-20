from django.contrib import admin
from .models import Event, EventRegistration

# Inline model for EventRegistration to show up in EventAdmin
class EventRegistrationInline(admin.TabularInline):
    model = EventRegistration
    extra = 0

# Admin for Event model to display event details and registration count
class EventAdmin(admin.ModelAdmin):
    inlines = [EventRegistrationInline]
    list_display = ('name', 'date', 'registration_count')

    # Custom method to display the registration count for an event
    def registration_count(self, obj):
        return EventRegistration.objects.filter(event=obj).count()

# Register Event and EventRegistration models in the admin site
admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration)
