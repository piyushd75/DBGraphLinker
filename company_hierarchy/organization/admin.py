from django.contrib import admin
from .models import Department, Team, Employee

# Register your models here.


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'department', 'team', 'supervisor')
    search_fields = ('name', 'employee_id')
