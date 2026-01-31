from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    staff_number = forms.CharField(required=False)  # optional because blank=True, null=True

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "staff_number")
