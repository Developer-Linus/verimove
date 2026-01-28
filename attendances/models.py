from django.db import models
from staffs.models import StaffModel
from vehicle_logs.models import CheckInModel

class SourceChoices(models.TextChoices):
    AUTO = "AUTO", "Automatic(Vehicle Entry)"
    MANUAL = "MANUAL", "Manual Entry"

class AttendanceRecordModel(models.Model):
    staff = models.ForeignKey(StaffModel, on_delete=models.CASCADE, related_name="attendance_records")
    date = models.DateField(db_index=True)
    first_checkin= models.ForeignKey(CheckInModel, on_delete=models.SET_NULL, null= True, blank=True, related_name = "attendance_first_checkin")
    source = models.CharField(choices=SourceChoices.choices, max_length=10, default=SourceChoices.AUTO)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        constraints= [
            models.UniqueConstraint(fields=["staff", "date"], name="unique_staff_attendance"),
            ]
        ordering= ["-date"]
    def __str__(self)->str:
        return f"{self.staff.staff_number} - {self.date} ({self.source})"