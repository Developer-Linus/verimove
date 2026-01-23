from django.urls import path, include
from rest_framework import routers
from .views import AllowanceViewSet
router = routers.DefaultRouter()
router.register(r'allowance', AllowanceViewSet)
urlpatterns = [path('api/v1/', include(router.urls)),]