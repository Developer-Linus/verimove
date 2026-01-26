from django.urls import path, include
from rest_framework import routers
from .views import AttendanceViewSet
router = routers.DefaultRouter()
router.register(r"attendances", AttendanceViewSet)
urlpatterns = [path("api/v1/", include(router.urls))]