from django.http import JsonResponse
from TODOApp.models import TodoItem
from TODOApp.serializers import TodoItemSerializer
from rest_framework import generics, permissions


# Create your views here.
def home(request):
    return JsonResponse({'message': 'Welcome to the TODO App!', 'data': [
        {'list of items': 'api/items/'},
        {'detail of item': 'api/items/<int:pk>/'}
    ]}, status=200)


class TodoItemView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [
        permissions.sessionAuthentication, permissions.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class TodoItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [
        permissions.sessionAuthentication, permissions.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
