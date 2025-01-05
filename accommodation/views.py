# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AccommodationForm

@login_required
def add_accommodation(request):
    if request.method == 'POST':
        form = AccommodationForm(request.POST)
        if form.is_valid():
            accommodation = form.save(commit=False)  # Don't save immediately
            accommodation.user = request.user  # Associate the accommodation with the logged-in user
            accommodation.save()  # Save the accommodation data to the database
            return redirect('home')  # Redirect to home after successful submission
    else:
        form = AccommodationForm()

    return render(request, 'add_accommodation.html', {'form': form})
