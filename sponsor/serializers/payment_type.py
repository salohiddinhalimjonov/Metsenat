from rest_framework import serializers
from sponsor.models.payment_type import PaymentType


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = [
            'id',
            'name'
        ]
