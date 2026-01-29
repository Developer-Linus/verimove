from django.urls import path, include
from rest_framework import routers
from .views import AllowanceViewSet, generate_allowances_view

app_name = "allowances"

router = routers.DefaultRouter()
router.register(r'allowances', AllowanceViewSet)
urlpatterns = [
    path('finance/generate/', generate_allowances_view, name="generate"),
    path('api/v1/', include(router.urls)),
    ]