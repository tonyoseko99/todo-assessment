from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
