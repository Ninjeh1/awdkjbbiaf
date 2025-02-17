from lib2to3.fixer_util import BlankLine

from django.db import models
from django.contrib.auth.models import User

class Penali(models.Model):

    SIDES = {'r': 'Right',
             'l': 'Left',
             'm': 'Middle'}
    scored = models.BooleanField(default=True)
    side = models.CharField(choices=SIDES,
                            max_length=1)
    player = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
