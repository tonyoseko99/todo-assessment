from rest_framework import serializers
from TODOApp.models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'title', 'description')
