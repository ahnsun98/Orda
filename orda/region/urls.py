from django.urls import path
from . import views

app_name = 'region'
urlpatterns = [
    path('main/', views.showmap),
]