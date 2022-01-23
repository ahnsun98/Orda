from django.urls import path
from . import views

app_name = 'info'
urlpatterns = [
    path('main/', views.main, name='main'),
]