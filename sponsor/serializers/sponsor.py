from rest_framework import serializers
from django.db.models import Sum
from sponsor.models.sponsor import Sponsor


class NewSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = [
            'id',
            'sponsor_type',
            'full_name',
            'phone_number',
            'payment_amount',
            'organization'
        ]


class SponsorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = [
            'full_name',
            'phone_number',
            'payment_amount',
            'sponsor_status'
        ]


class SponsorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = [
            'id',
            'sponsor_type',
            'full_name',
            'phone_number',
            'sponsor_status',
            'payment_amount',
            'payment_type'
        ]


class SponsorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = [
            'id',
            'full_name',
            'phone_number',
            'payment_amount',
            'created_datetime',
            'sponsor_status'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['spent_money'] = instance.payment_of.aggregate(spent_money=Sum('given_money')).get('spent_money')
        return representation


__all__ = ['NewSponsorSerializer', 'SponsorProfileSerializer', 'SponsorListSerializer', 'SponsorUpdateSerializer']
