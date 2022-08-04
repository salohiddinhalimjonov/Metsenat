from rest_framework import serializers
from payment.models.payment import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = [
            'id',
            'sponsor',
            'given_money'
        ]
