

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    asignee = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
