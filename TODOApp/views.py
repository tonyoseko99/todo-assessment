from rest_framework import generics, permissions
from .models import TodoItem
from .serializers import TodoItemSerializer

# Create your views here.


class TodoItemList(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TodoItem.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
