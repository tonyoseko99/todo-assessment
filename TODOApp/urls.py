from django.urls import path
from TODOApp import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    # path('', views.home, name='home'),
    path('items/', views.TodoItemList.as_view(), name='todoitems-all'),
    path('items/<int:pk>/', views.TodoItemDetailView.as_view(),
         name='todoitems-detail'),
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api-token-auth'),
    path('signup/', views.SignupView.as_view(), name='signup'),
]
