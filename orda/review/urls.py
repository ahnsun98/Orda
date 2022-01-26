from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('post/', views.post, name='post'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('post/<int:id>', views.detail, name='detail'),
    path('delete/<int:id>', views.delete, name='delete'),
]