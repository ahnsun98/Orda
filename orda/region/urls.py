from django.urls import path
from . import views

app_name = 'region'
urlpatterns = [
    path('region/', views.showmap),

]