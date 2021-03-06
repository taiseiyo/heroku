#!/usr/bin/env python3
from django.db import models

# Create your models here.

# use DiaryView and RegisterView in views.py


class ActiveUser(models.Model):
    name = models.CharField(max_length=20)
    mail = models.EmailField(max_length=40)

    def __str__(self):
        return self.name + " mail address: " + self.mail
