from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, EventRegistration

def event_register(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    info = None  # Default info message

    if not request.user.is_authenticated:
        return render(request, 'login.html', {'info': 'You must be logged in to register for an event.'})

    if request.method == 'POST':
        if EventRegistration.objects.filter(event=event, student=request.user).exists():
            info = 'Already registered !!!'
        else:
            EventRegistration.objects.create(event=event, student=request.user)
            info = f'You have successfully registered for {event.name}!'

    return render(request, 'event_register.html', {'event': event, 'info': info})

def event(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events})
