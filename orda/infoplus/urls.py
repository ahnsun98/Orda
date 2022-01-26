from django.urls import path
from . import views

urlpatterns = [
    path('food/', views.food),  
    path('insta/', views.insta),
    path('button/', views.button),
]
