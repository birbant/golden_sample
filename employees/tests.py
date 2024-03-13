from .models import Employees
from django.test import TestCase, RequestFactory
# from django.urls import reverse
# from django.contrib.auth.models import User
# from .views import employee_delete

"""testing model Employees"""


class EmployeesModelTestCase(TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.factory = None
        self.user = None

    def setUp(self):
        self.employee = Employees.objects.create(
            first_name='John',
            last_name='Doe',
            employee_id=12345,
            department='quality'
        )

    def test_employee_creation(self):
        self.assertTrue(isinstance(self.employee, Employees))
        self.assertEqual(self.employee.__str__(), f"{self.employee.employee_id}")

    def test_employee_fields(self):
        self.assertEqual(self.employee.first_name, 'John')
        self.assertEqual(self.employee.last_name, 'Doe')
        self.assertEqual(self.employee.employee_id, 12345)
        self.assertEqual(self.employee.department, "quality")

    def test_employee_department_choices(self):
        # Test whether department is among options
        department_choices = dict(Employees.STATUS_CHOICES)
        self.assertIn(self.employee.department, department_choices.values())

    def test_employee_id_uniqueness(self):
        # Is ID unique
        with self.assertRaises(Exception):
            Employees.objects.create(
                first_name='Jane',
                last_name='Smith',
                employee_id=12345,  # The same ID as previous
                department='projects'
            )

    def test_employee_string_representation(self):
        expected_string = f"{self.employee.employee_id}"
        self.assertEqual(str(self.employee), expected_string)
