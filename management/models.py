from django.db import models
from samples.models import Samples
from employees.models import Employees


class SampleOperation(models.Model):
    COLLECTION = 'Collection'
    RETURN = 'Return'
    Operation_type = [
        (COLLECTION, 'Collection'),
        (RETURN, 'Return'),
    ]
    sample_id = models.ForeignKey(Samples, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    operation_type = models.CharField(max_length=20, choices=Operation_type)
    operation_date = models.DateTimeField(unique=False, error_messages={'required': "Please fill in this field."})
    production_order = models.CharField(max_length=50, null=True, blank=True)
    storage_place = models.CharField(max_length=50, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.operation_type == self.COLLECTION:
            # Jeśli wybrano Collection i podano production_order
            if self.production_order:
                self.storage_place = 'PRODUCTION'
            else:
                # Jeśli wybrano Collection, ale nie podano production_order,
                # ustaw storage_place na department_id pracownika, który pobiera
                self.storage_place = self.employee_id.department
        if self.operation_type == self.RETURN:
            sample = self.sample_id
            self.storage_place = sample.storage_place
        super().save(*args, **kwargs)
