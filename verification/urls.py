from django.urls import path
from .views import ALPRCaptureAPIView

urlpatterns = [
    path('api/verification/capture/', ALPRCaptureAPIView.as_view(), name='alpr_capture'),
]