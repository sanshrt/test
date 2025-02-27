"""
URL configuration for shackles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from office_bearers.views import *
from events.views import *
from contact.views import *
from accommodation.views import *
from workshop.views import *
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('pay/', pay, name='pay'), 
    path('register/', reg, name='register'),
    path('team/',team,name='team'),
    path('event/',event,name='event'),
    path('events/register/<int:event_id>/', event_register, name='event_register'),
    path('logout/',logout_view, name='logout'),
    path('send_message/',send_message, name='send_message'),
    path('my_messages/',my_messages, name='my_messages'),
    path('contact/',contact,name='contact'),
    path('accommodation/',add_accommodation, name='accommodation'),
     path('workshop/', workshop, name='workshop_list'),  # URL for the workshop list
    path('workshop/register/<int:pk>/',register_workshop, name='register_workshop'),  # URL for workshop registration
    path('workshop/payment/<int:pk>/', workshop_payment, name='workshop_payment'), 

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
