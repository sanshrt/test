from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Event, EventRegistration

def event_register(request, event_id):
    # Retrieve the event object using the provided event_id
    event = Event.objects.get(id=event_id)

    # Check if the user is logged in
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to register for an event.')
        return redirect('login')  # Redirect to login page if the user is not authenticated

    # Handle POST request when the user submits the registration form
    if request.method == 'POST':
        # Check if the user is already registered for the event
        if EventRegistration.objects.filter(event=event, student=request.user).exists():
            messages.warning(request, 'You are already registered for this event.')
            return redirect('event_register', event_id=event_id)

        # Register the user for the event
        EventRegistration.objects.create(event=event, student=request.user)

        # Show a success message
        messages.success(request, f'You have successfully registered for {event.name}!')
        return redirect('event_register', event_id=event_id)

    # Return the event registration page with event details
    return render(request, 'event_register.html', {'event': event})

def event(request):
    # Retrieve all events to display on the event listing page
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events})
