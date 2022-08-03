from rest_framework.viewsets import ModelViewSet
from sponsor.models.payment_type import PaymentType
from sponsor.serializers.payment_type import PaymentTypeSerializer


class PaymentTypeViewSet(ModelViewSet):
    serializer_class = PaymentTypeSerializer

    def get_queryset(self):
        return PaymentType.objects.all()
