from django import forms
from .models import SampleOperation


class SampleOperationAdder(forms.ModelForm):
    class Meta:
        model = SampleOperation
        fields = '__all__'

        widgets = {
            'operation_date': forms.DateInput(attrs={'type': 'date'}),
        }
        input_formats = ['%Y-%m-%d']
