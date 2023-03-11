# app urls

# Path: TODOApp/urls.py
from django.urls import path
from TODOApp import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.TodoItemView.as_view(), name='todoitems-all'),
    path('items/<int:pk>/', views.TodoItemDetailView.as_view(),
         name='todoitems-detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api-token-auth/<str:username>/',
         views.GenerateTokenView.as_view(), name='api_token_auth'),
]
