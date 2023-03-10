from django.shortcuts import render
from TODOApp.models import TodoItem
from TODOApp.serializers import TodoItemSerializer
from rest_framework import generics


# Create your views here.

class TodoItemView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer