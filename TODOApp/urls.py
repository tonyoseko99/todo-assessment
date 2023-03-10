# app urls

# Path: TODOApp/urls.py
from django.urls import path
from TODOApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.TodoItemView.as_view(), name='todoitems-all'),
    path('items/<int:pk>/', views.TodoItemDetailView.as_view(),
         name='todoitems-detail'),
]
