from datetime import date
from decimal import Decimal

from django.db import transaction
from django.db.models import Count

from allowances.models import AllowanceModel
from attendances.models import AttendanceRecordModel
from staffs.models import StaffModel


def month_start(d: date) -> date:
    return d.replace(day=1)


def next_month_start(d: date) -> date:
    if d.month == 12:
        return date(d.year + 1, 1, 1)
    return date(d.year, d.month + 1, 1)


@transaction.atomic
def generate_allowances_for_month(*, month: date, rate_per_day: Decimal) -> dict:
    """Generate allowances for all eligible staff for a given month."""
    month = month_start(month)
    start = month
    end = next_month_start(month)

    # 1) Eligible staff ids
    eligible_ids = list(
        StaffModel.objects.filter(
            is_active=True,
            is_allowance_legible=True,
        ).values_list("id", flat=True)
    )

    if not eligible_ids:
        return {"eligible": 0, "created": 0, "updated": 0, "skipped_paid": 0}

    # 2) Count attendance days per staff (ONE query)
    attendance_counts = (
        AttendanceRecordModel.objects.filter(
            staff_id__in=eligible_ids,
            date__gte=start,
            date__lt=end,
        )
        .values("staff_id")
        .annotate(days_present=Count("id"))
    )
    days_by_staff = {row["staff_id"]: row["days_present"] for row in attendance_counts}

    # 3) Existing allowances for that month (ONE query)
    existing_allowances = {
        a.staff_id: a
        for a in AllowanceModel.objects.filter(
            staff_id__in=eligible_ids,
            month=month,
        )
    }

    to_create = []
    to_update = []

    created = 0
    updated = 0
    skipped_paid = 0

    # 4) Build create/update lists (NO DB writes here)
    for staff_id in eligible_ids:
        days_present = days_by_staff.get(staff_id, 0)
        allowance = existing_allowances.get(staff_id)

        if allowance is None:
            to_create.append(
                AllowanceModel(
                    staff_id=staff_id,
                    month=month,  # already normalized
                    days_present=days_present,
                    rate_per_day=rate_per_day,
                    total_amount=days_present * rate_per_day,
                )
            )
            created += 1
        else:
            if allowance.status == "PAID":
                skipped_paid += 1
                continue

            allowance.days_present = days_present
            allowance.rate_per_day = rate_per_day
            allowance.total_amount = days_present * rate_per_day
            to_update.append(allowance)
            updated += 1

    # 5) Bulk write ONCE
    if to_create:
        AllowanceModel.objects.bulk_create(to_create, batch_size=1000)

    if to_update:
        AllowanceModel.objects.bulk_update(
            to_update,
            ["days_present", "rate_per_day", "total_amount"],
            batch_size=1000,
        )

    return {
        "eligible": len(eligible_ids),
        "created": created,
        "updated": updated,
        "skipped_paid": skipped_paid,
    }
