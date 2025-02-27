from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import RegisterForm
from .models import Register
from payment.models import Payment

# Home page view
def home(request):
    user = Register.objects.first() 
    if request.user.is_authenticated:
        return render(request, 'home.html', {'user': request.user,'username': user.name})
    else:
        return redirect('login')

# Registration view
def reg(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pay')  # Redirect to the payment page
        else:
            print(form.errors)
            return render(request, 'register.html', {'form': form, 'info': 'Invalid registration details'})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

# Login view
def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')  
        password = request.POST.get('password')
        
        user = authenticate(username=user_name, password=password)
        
        if user is not None:
            payment = Payment.objects.filter(user=user).first()
            if payment is None:
                return render(request, 'login.html', {'info': 'Payment not received'})
            
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'info': 'Invalid credentials. Please try again.'})
    
    return render(request, 'login.html')

# Logout view
def logout_view(request):
    auth_logout(request)
    return redirect('login')

# Payment page view
def pay(request):
    return render(request, 'pay.html')
    
