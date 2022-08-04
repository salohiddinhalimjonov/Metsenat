from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payment.views.payment import PaymentViewSet
from payment.views.statistics import StatisticsView, StudentSponsorCount

router = DefaultRouter()
router.register('', PaymentViewSet, basename='payment')

urlpatterns = [
    path('statistics/', StatisticsView.as_view()),
    path('student_sponsor_count/', StudentSponsorCount.as_view()),
    path('', include(router.urls))
]
