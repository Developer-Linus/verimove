from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    """
    Displays a signup form (GET) and creates a new user (POST).

    After a successful signup:
      1) Saves the user (handled by CreateView + form.save()).
      2) Logs the user in immediately.
      3) Adds a success message.
      4) Redirects to success_url.
    """

    # The form that creates your CustomUser (swapped user model).
    form_class = CustomUserCreationForm

    # The template that renders the signup page.
    template_name = "accounts/signup.html"

    # Where to redirect after successful registration.
    # reverse_lazy is used because class attributes are evaluated at import time.
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        """
        Called when the submitted form is valid.
        This is the best place to hook in extra actions after saving the user.
        """

        # Let CreateView handle saving the user and setting self.object
        # self.object becomes the newly created user instance.
        response = super().form_valid(form)

        # Log the new user in (creates a session immediately).
        # self.object is the created user.
        login(self.request, self.object)

        # Add a one-time "flash" message shown on the next page load.
        messages.success(self.request, "Account created successfully. Welcome!")

        # Continue with the normal redirect (success_url).
        return response

    def form_invalid(self, form):
        """
        Called when the submitted form has errors.
        Optional: add a friendly message. The form errors will still show.
        """
        messages.error(self.request, "Please correct the errors below and try again.")
        return super().form_invalid(form)
