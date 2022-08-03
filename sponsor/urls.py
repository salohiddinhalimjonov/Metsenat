from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views.payment_type import PaymentTypeViewSet
from views.sponsor import SponsorViewSet

router = DefaultRouter()
router.register('payment_type/', PaymentTypeViewSet, basename='payment_type')
router.register('', SponsorViewSet, basename='sponsor')

urlpatterns = [
    path('', include(router.urls))
]
