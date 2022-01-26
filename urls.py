from django.urls import path
from . import views 

urlpatterns = [
     path('',views.home),
     path('signin',views.signin),
     path('signup',views.signup),
     path('home',views.home),
     path('ticket booking',views.ticket_booking),
     path('fare_calculation',views.fare_calculation)
    
]