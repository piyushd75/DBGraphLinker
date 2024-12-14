from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teams')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.department.name}"


class Employee(models.Model):
    name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=20, unique=True)
    position = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)  # New field for address
    hire_date = models.DateField(null=True, blank=True)  # New field for hire date
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    supervisor = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subordinates')

    def __str__(self):
        return f"{self.name} ({self.position})"

