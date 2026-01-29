from datetime import datetime, date
from decimal import Decimal
from django import forms

class GenerateAllowancesForm(forms.Form):
    month = forms.CharField(
        label="Month",
        widget=forms.TextInput(attrs={
            "type": "month", 
            "class": "form-control"
        }),
        help_text="Select the month to generate allowances for.",
    )

    rate_per_day = forms.DecimalField(
        label="Rate per day",
        max_digits=12,
        decimal_places=2,
        min_value=Decimal("0.00"),
        initial=Decimal("0.00"), # Helps avoid NoneType errors in templates
        widget=forms.NumberInput(attrs={
            "step": "0.01", 
            "class": "form-control"
        }),
    )

    def clean_month(self):
        data = self.cleaned_data.get("month")
        if not data:
            raise forms.ValidationError("This field is required.")

        try:
            parsed_date = datetime.strptime(data, "%Y-%m").date()
            return parsed_date
        except (ValueError, TypeError):
            raise forms.ValidationError(
                "Invalid month format. Please use the date picker (YYYY-MM)."
            )