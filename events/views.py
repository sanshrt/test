from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Event, EventRegistration

def event_register(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to register for an event.')
        return redirect('login')

    if request.method == 'POST':
        if EventRegistration.objects.filter(event=event, student=request.user).exists():
            messages.warning(request, 'You are already registered for this event.')
        else:
            EventRegistration.objects.create(event=event, student=request.user)
            messages.success(request, f'You have successfully registered for {event.name}!')
        return redirect('event_register', event_id=event_id)

    return render(request, 'event_register.html', {'event': event})

def event(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events})
