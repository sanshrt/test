from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm  # Assuming you have a form to handle the message input.

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user  # Set the logged-in user as the message sender.
            message.save()
            return redirect('my_messages')  # Redirect to the page where the user can see their messages.
    else:
        form = MessageForm()

    return render(request, 'send_message.html', {'form': form})

@login_required
def my_messages(request):
    messages = Message.objects.filter(user=request.user).order_by('-timestamp')  # Get messages for the logged-in user.
    return render(request, 'my_messages.html', {'messages': messages})


def contact(request):
    return render(request,'contact.html')