from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('accounts/signup/', RegisterView.as_view(), name='signup'),
]