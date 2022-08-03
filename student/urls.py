from django.urls import path, include
from rest_framework.routers import DefaultRouter
from student.views.otm import OTMViewSet
from student.views.student import StudentViewSet
from student.views.student_type import StudentTypeViewSet

router = DefaultRouter()
router.register('otm/', OTMViewSet, basename='otm')
router.register('', StudentViewSet, basename='student')
router.register('student_type', StudentTypeViewSet, basename='student_type')

urlpatterns = [
    path('', include(router.urls))
]
