from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Employees(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    employee_id = models.IntegerField(validators=[MinValueValidator(10000), MaxValueValidator(99999)], unique=True)
    STATUS_CHOICES = [
        ('quality', 'Quality'),
        ('projects', 'Projects'),
        ('tool-house', 'Tool-house'),
        ('technical', 'Technical'),
        ('other', 'Other'),
    ]
    department = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return str(self.employee_id)

    class Meta:
        verbose_name = "Employees"
        verbose_name_plural = "Employees"