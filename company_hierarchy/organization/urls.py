from django.urls import path
from . import views

urlpatterns = [
    path('hierarchy/', views.employee_hierarchy, name='employee_hierarchy'),
    path('departments/', views.department_list, name='department_list'),
]
