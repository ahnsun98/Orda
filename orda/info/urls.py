from django.urls import path
from . import views

urlpatterns = [
    path('food/', views.food),
    path('mountain/', views.mountain),
   
]
