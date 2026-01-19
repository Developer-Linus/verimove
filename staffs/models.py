from django.db import models
from django.utils import timezone

class StaffModel(models.Model):
    staff_number = models.CharField(max_length=255,db_index=True,unique=True)
    full_name = models.CharField(max_length=255)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_allowance_legible = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Staff"
    def __str__(self)->str:
        return f"{self.full_name} ({self.staff_number})"