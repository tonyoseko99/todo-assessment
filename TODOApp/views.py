from TODOApp.models import TodoItem
from TODOApp.serializers import TodoItemSerializer
from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated


class ItemsView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class TodoItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
