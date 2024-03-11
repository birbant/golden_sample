from django.forms import ModelForm
from .models import Employees


class EmployeeAdder(ModelForm):

    class Meta:
        model = Employees
        fields = '__all__'