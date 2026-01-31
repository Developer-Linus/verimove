from django.shortcuts import render
from staffs.models import StaffModel
from vehicle_logs.models import CheckInModel
from allowances.models import AllowanceModel
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied

# Function to check if user is Finance or Admin
def is_finance_staff(user):
    if user.is_superuser or user.groups.filter(name='Finance').exists():
        return True
    raise PermissionDenied


def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')



@login_required
@user_passes_test(is_finance_staff)
def dashboard(request):
    # 1. Today's Check-ins
    today = timezone.now().date()
    today_checkins = CheckInModel.objects.filter(timestamp__date=today).count()
    
    # 2. Total Staff Count
    staff_count = StaffModel.objects.filter(is_active=True).count()
    
    # 3. Pending Payouts
    pending_data = AllowanceModel.objects.filter(status='pending').aggregate(Sum('total_amount'))
    pending_total = pending_data['total_amount__sum'] or 0
    
    context = {
        'today_checkins': today_checkins,
        'staff_count': staff_count,
        'pending_payouts': f"{pending_total:,.2f}",
    }
    
    return render(request, 'dashboard.html', context)