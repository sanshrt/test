from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

def workshop(request):
    workshops = Workshop.objects.all()
    registered_workshops = []

    if request.user.is_authenticated:
        # Get a list of workshops the user is already registered for
        registered_workshops = WorkshopRegister.objects.filter(student=request.user).values_list('workshop', flat=True)

    return render(request, 'workshop.html', {
        'workshop': workshops,
        'registered_workshops': registered_workshops
    })


@login_required
def register_workshop(request, pk):
    # Fetch the specific workshop
    workshop = get_object_or_404(Workshop, pk=pk)

    # Check if the user is already registered
    already_registered = WorkshopRegister.objects.filter(student=request.user, workshop=workshop).exists()

    if already_registered:
        # Pass a flag to the template to indicate registration status
        return render(request, 'workshop.html', {'workshop': Workshop.objects.all(), 'is_registered': True})
    
    # Register the user with pay=False by default
    WorkshopRegister.objects.create(student=request.user, workshop=workshop)
    messages.success(request, "Registration successful! Redirecting to the payment page.")
    return redirect('workshop_payment', pk=workshop.id)

@login_required
def workshop_payment(request, pk):
    # Fetch the specific workshop
    workshop = get_object_or_404(Workshop, pk=pk)

    # Ensure the user is registered for the workshop
    if not WorkshopRegister.objects.filter(student=request.user, workshop=workshop).exists():
        messages.error(request, "You need to register for the workshop first.")
        return redirect('workshop_list')

    return render(request, 'workshop_payment.html', {'workshop': workshop})
