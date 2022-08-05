from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sponsor.views.payment_type import PaymentTypeViewSet
from sponsor.views.sponsor import SponsorViewSet

router = DefaultRouter()
router.register('payment_type', PaymentTypeViewSet, basename='payment_type')
router.register('main', SponsorViewSet, basename='sponsor')

urlpatterns = [
    path('', include(router.urls))
]
