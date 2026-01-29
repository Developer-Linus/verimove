from django.shortcuts import render
# Importing based on the app names and model names you provided
from staffs.models import StaffModel
from vehicle_logs.models import CheckInModel  # Adjust folder name if 'Vehicle Logs' uses an underscore
from allowances.models import AllowanceModel


def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

from django.utils import timezone
from django.db.models import Sum



def dashboard(request):
    # 1. Today's Check-ins (from Vehicle Logs app)
    today = timezone.now().date()
    # We count unique staff check-ins for today
    today_checkins = CheckInModel.objects.filter(timestamp__date=today).count()
    
    # 2. Total Staff Count (from Staffs app)
    staff_count = StaffModel.objects.filter(is_active=True).count()
    
    # 3. Pending Payouts (from Allowances app)
    # We sum the 'total_amount' where status is 'pending'
    pending_data = AllowanceModel.objects.filter(status='pending').aggregate(Sum('total_amount'))
    pending_total = pending_data['total_amount__sum'] or 0
    
    context = {
        'today_checkins': today_checkins,
        'staff_count': staff_count,
        'pending_payouts': f"{pending_total:,.2f}",
    }
    
    return render(request, 'dashboard.html', context)