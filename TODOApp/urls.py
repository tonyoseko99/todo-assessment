# app urls

# Path: TODOApp/urls.py
from django.urls import path
from TODOApp import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    # path('', views.home, name='home'),
    path('items/', views.TodoItemList.as_view(), name='todoitems-all'),
    path('items/<int:pk>/', views.TodoItemDetailView.as_view(),
         name='todoitems-detail'),
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api-token-auth'),
    path('login/', views.CreateUserView.as_view(), name='login'),
    path('users/', views.UserList.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]
