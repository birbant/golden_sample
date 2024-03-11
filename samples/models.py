from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


class Samples(models.Model):
    part_number = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(99999)], unique=True)
    part_name = models.CharField(max_length=255, unique=False)
    drawing_number = models.CharField(max_length=20, unique=False)
    drawing_revision = models.CharField(max_length=20, unique=False)
    client = models.CharField(max_length=125)
    trial_number = models.CharField(max_length=20, unique=True)
    APPROVED = 'Approved'
    NOT_APPROVED = 'Not approved'
    STATUS_CHOICES = [
            (APPROVED, 'Approved'),
            (NOT_APPROVED, 'Not approved'),
        ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not approved')
    approval_date = models.DateField(blank=True, null=True)
    storage_place = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.part_name

    def clean(self):
        if self.status == self.APPROVED and not self.approval_date:
            raise ValidationError({'approval_date': "Approval date is required when status is 'Approved'."})

    class Meta:
        verbose_name = "Samples"
        verbose_name_plural = "Samples"