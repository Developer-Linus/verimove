from django.urls import path, include
from rest_framework import routers
from .views import StaffViewSet
router = routers.DefaultRouter()
router.register(r'staffs', StaffViewSet)
urlpatterns = [path('api/v1/staffs/', include(router.urls)),]