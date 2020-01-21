from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as v


router = DefaultRouter(trailing_slash=False)
router.register(r'attendance-places', v.AttendancePlaceViewSet)
router.register(r'attendance-times', v.AttendanceTimeViewSet)
router.register(r'attendance-rules', v.AttendanceRuleViewSet)

urlpatterns = [
    path('', include(router.urls))
]
