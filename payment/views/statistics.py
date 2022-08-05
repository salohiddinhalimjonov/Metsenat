from decimal import Decimal
from django.db.models import Sum, Count
from django.db.models.functions import Coalesce
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from payment.serializers.statistics import StatisticsSerializer
from payment.models.payment import Payment
from sponsor.models.sponsor import Sponsor
from student.models.student import Student


class StatisticsView(APIView):

    def get(self, request):
        data = {}
        paid_money = Payment.objects.aggregate(paid_money=Coalesce(Sum('given_money'), Decimal(0))).get('paid_money')
        requested_money = Student.objects.aggregate(requested_money=Coalesce(Sum('tuition_fee'), Decimal(0))).get('requested_money')
        must_pay = requested_money - paid_money
        data['paid_money'] = paid_money
        data['requested_money'] = requested_money
        data['must_pay'] = must_pay
        return Response(data, status=status.HTTP_200_OK)


class StudentSponsorCount(APIView):

    def get(self, request):
        data = {}
        serializer = StatisticsSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        date = serializer.validated_data.get('date')
        students_count = Student.objects.filter(created_datetime__lte=date).aggregate(students_count=Count('id')).get('students_count')
        sponsors_count = Sponsor.objects.filter(created_datetime__lte=date).aggregate(sponsors_count=Count('id')).get('sponsors_count')
        data['sponsors_count'] = sponsors_count
        data['students_count'] = students_count
        return Response(data, status=status.HTTP_200_OK)