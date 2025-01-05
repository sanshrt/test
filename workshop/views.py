from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Workshop, WorkshopRegistration

def workshop_list(request):
    workshops = Workshop.objects.all()
    return render(request, 'workshop_list.html', {'workshops': workshops})

@login_required
def register_workshop(request, workshop_id):
    workshop = get_object_or_404(Workshop, id=workshop_id)
    if request.method == 'POST':
        registration, created = WorkshopRegistration.objects.get_or_create(
            user=request.user,
            workshop=workshop
        )
        if created:
            messages.success(request, f"Successfully registered for {workshop.title}")
            return redirect('pay')  # Redirect to the payment page or dashboard
        else:
            messages.info(request, f"You are already registered for {workshop.title}")
            return redirect('workshop_list')

    return render(request, 'register_workshop.html', {'workshop': workshop})
