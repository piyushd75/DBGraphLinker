from django.core.management.base import BaseCommand
from organization.models import Department, Team, Employee
import random
from faker import Faker


class Command(BaseCommand):
    help = "Populate the database with sample data for departments, teams, and employees"

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting to load sample data...")

        # Clear existing data
        Employee.objects.all().delete()
        Team.objects.all().delete()
        Department.objects.all().delete()

        # Create Departments
        departments = [
            {"name": "Engineering", "description": "Handles all technical projects."},
            {"name": "Human Resources", "description": "Manages recruitment and people development."},
            {"name": "Finance", "description": "Manages financial transactions and budgets."},
        ]
        department_objs = []
        for data in departments:
            department = Department.objects.create(**data)
            department_objs.append(department)
        self.stdout.write("Departments created.")

        # Create Teams
        teams = [
            {"name": "Backend Team", "department": department_objs[0]},
            {"name": "Frontend Team", "department": department_objs[0]},
            {"name": "Recruitment Team", "department": department_objs[1]},
            {"name": "Accounts Team", "department": department_objs[2]},
        ]
        team_objs = []
        for data in teams:
            team = Team.objects.create(**data)
            team_objs.append(team)
        self.stdout.write("Teams created.")

        # Create Employees
        fake = Faker()
        employees = [
            {"name": "Alice Smith", "employee_id": "EMP001", "position": "Backend Engineer", "team": team_objs[0]},
            {"name": "Bob Johnson", "employee_id": "EMP002", "position": "Frontend Engineer", "team": team_objs[1]},
            {"name": "Charlie Brown", "employee_id": "EMP003", "position": "HR Manager", "team": team_objs[2]},
            {"name": "David Wilson", "employee_id": "EMP004", "position": "Accountant", "team": team_objs[3]},
        ]

        employee_objs = []
        for data in employees:
            supervisor = random.choice(employee_objs) if employee_objs else None
            employee = Employee.objects.create(
                name=data['name'],
                employee_id=data['employee_id'],
                position=data['position'],
                team=data['team'],
                department=data['team'].department,
                supervisor=supervisor,
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.address(),
                hire_date=fake.date_this_decade()
            )
            employee_objs.append(employee)
        self.stdout.write("Employees created.")

        self.stdout.write(self.style.SUCCESS("Sample data loaded successfully!"))
