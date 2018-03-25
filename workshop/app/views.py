# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from app.models import Department, Student
from app.util import fx
# Create your views here.

def homepage(request):
    # qs = Department.objects.all().values('name', 'id')
    stud = Student.objects.get(pk=1)
    print(stud.department.name)
    print(fx())
    # return render(request, 'base.html', {'qs': qs})
    return render(request, 'base.html')



    # return HttpResponse('<h1>Hello</h1>')