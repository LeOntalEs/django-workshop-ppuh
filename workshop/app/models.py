# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=64)
    department = models.OneToOneField(Department)

    def __str__(self):
        return self.name