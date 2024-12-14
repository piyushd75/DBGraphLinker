from django.shortcuts import render
from .models import Employee
from .models import Department
# Create your views here.


def employee_hierarchy(request):
    employees = Employee.objects.all()
    return render(request, 'organization/hierarchy.html', {'employees': employees})


def department_list(request):
    departments = Department.objects.all()  # Fetch all departments
    context = {
        'departments': departments  # Context data passed to the template
    }
    return render(request, 'organization/department_list.html', context)
