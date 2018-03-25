# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models import Department, Student
# Register your modedls here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Department._meta.fields]
    list_editable = [f.name for f in Department._meta.fields \
        if f.name not in ['id']]

admin.site.register(Student)
admin.site.register(Department, DepartmentAdmin)