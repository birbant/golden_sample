from django import forms
from .models import Samples


class SamplesAdder(forms.ModelForm):
    class Meta:
        model = Samples
        fields = '__all__'

        widgets = {
            'approval_date': forms.DateInput(attrs={'type': 'date'}),
        }
        input_formats = ['%Y-%m-%d']
