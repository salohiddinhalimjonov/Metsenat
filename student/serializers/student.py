from decimal import Decimal
from django.db.models import Sum
from django.db.models.functions import Coalesce
from rest_framework import serializers
from student.models.student import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'full_name',
            'phone_number',
            'otm',
            'student_type',
            'tuition_fee'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['recieved_money'] = instance.payments_for.aggregate(
            recieved_money=Coalesce(Sum('given_money'), Decimal(0))).get('recieved_money')
        return representation


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'full_name',
            'phone_number',
            'otm',
            'tuition_fee'
        ]
