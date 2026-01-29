from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .serializers import AllowanceModelSerializer
from rest_framework import viewsets
from .models import AllowanceModel

from allowances.forms import GenerateAllowancesForm
from allowances.services import generate_allowances_for_month
class AllowanceViewSet(viewsets.ModelViewSet):
    queryset = AllowanceModel.objects.all()
    serializer_class = AllowanceModelSerializer


# @login_required  # Recommended for data-modifying views
def generate_allowances_view(request):
    if request.method == "POST":
        form = GenerateAllowancesForm(request.POST)
        if form.is_valid():
            try:
                month = form.cleaned_data["month"]
                rate_per_day = form.cleaned_data["rate_per_day"]

                result = generate_allowances_for_month(month=month, rate_per_day=rate_per_day)

                messages.success(
                    request,
                    f"Allowance generation complete for {month:%Y-%m}. "
                    f"Eligible={result['eligible']}, Created={result['created']}, "
                    f"Updated={result['updated']}, Skipped(PAID)={result['skipped_paid']}."
                )
                # Redirect to avoid form re-submission on refresh
                return redirect("allowances:generate") 

            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
    else:
        form = GenerateAllowancesForm()

    return render(
        request,
        "allowances/generate_allowances.html",
        {"form": form},
    )
