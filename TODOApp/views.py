from django.http import JsonResponse
from django.shortcuts import render
from TODOApp.models import TodoItem
from TODOApp.serializers import TodoItemSerializer
from rest_framework import generics


# Create your views here.
def home(request):
    return JsonResponse({'message': 'Welcome to the TODO App!', 'data': [
        {'list of items': 'api/items/'},
        {'detail of item': 'api/items/<int:pk>/'}
    ]}, status=200)


class TodoItemView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class TodoItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
