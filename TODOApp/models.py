from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='todo_items')

    def __str__(self):
        return self.title
