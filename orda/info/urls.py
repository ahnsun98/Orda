from django.urls import path
from . import views

app_name = 'info'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('list/', views.list, name='list'),
    path('imglist/', views.imglist, name='imglist'),
]
