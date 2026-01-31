from datetime import time
from django.utils import timezone
from django.db import transaction
from vehicle_logs.models import CheckInModel
from attendances.models import AttendanceRecordModel
from vehicles.models import VehicleModel

class ALPRProcessing:
    @staticmethod
    def process_capture(plate_text, image_file=None, gate_name = "Main Gate"):
        """
        Approach:
        1. Normalize plate and identity staff
        2. Create a CheckInModel (Security Audit).
        3. Check 06:00 - 18:00 window.
        4. Create AttendanceModel if it's the first check-in of the day.
        """
        # Convert it to 'Africa/Nairobi' as specified in settings.py
        now_local = timezone.localtime(timezone.now())
        current_time = now_local.time()
        today = now_local.date()

        # Normalize plate text for database matching
        clean_plate = "".join(plate_text.split()).upper()

        # Step 1: Identification
        vehicle = VehicleModel.objects.filter(plate_number=clean_plate).first()
        staff = vehicle.staff_id if vehicle else None

        # Step 2: Persistent security logging
        # Every car gets a record regardless of staff and time
        with transaction.atomic():
            checkin_log = CheckInModel.objects.create(
                plate_number = clean_plate,
                vehicle = vehicle,
                staff = staff,
                gate = gate_name,
                direction = "IN",
                image = image_file
            )
        # Step 3: Working Hours validation (6:00AM - 6:00PM)
        start_work = time(6,0)
        end_work = time(18,0)
        if staff and start_work <= current_time <= end_work:
            # Step 4: Idempotency (UniqueConstraint check)
            attendance_exists = AttendanceRecordModel.objects.filter(
                staff=staff,
                date=today).exists()
            if not attendance_exists:
                AttendanceRecordModel.objects.create(
                    staff=staff,
                    date=today,
                    first_checkin = checkin_log,
                    source="AUTO",
                )
                return f"SUCCESS: {staff.full_name} checked in at {current_time} on {today}"
            return f"INFO: {staff.full_name} already checked in on {today}"
        return "SUCCESS: Universal log created. No attendance required."