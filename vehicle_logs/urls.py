from django.urls import path, include
from rest_framework import routers
from .views import CheckInViewSet
router = routers.DefaultRouter()
router.register(r'vehicle_logs', CheckInViewSet)
urlpatterns = [path('api/v1/', include(router.urls)),]