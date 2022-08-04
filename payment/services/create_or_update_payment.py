from django.db.models import Sum
from rest_framework import status
from rest_framework.response import Response
from sponsor.models.sponsor import Sponsor


def create_or_update_payment(student, serializer):
    sponsor = serializer.validated_data.get('sponsor')
    given_money = serializer.validated_data.get('given_money')
    sum_of_student_money = student.payment_for.aggregate(sum_money=Sum(given_money)).get('sum_money')
    added_student_money = sum_of_student_money + given_money

    if added_student_money > student.tuition_fee:
        return Response({'detail': 'that amount of money is a lot for paying the tuition fee of the student!'},
                        status=status.HTTP_400_BAD_REQUEST)

    if sponsor.payment_amount >= given_money:
        serializer.save()
        sponsor.payment_amount -= given_money
        sponsor.sponsor_status = Sponsor.TASDIQLANGAN
        sponsor.save(update_fields=['payment_amount', 'sponsor_status'])
        return Response({'status': 'payment has benn saved successfully!'}, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'the sponsor does not have that amount of money!'},
                        status=status.HTTP_400_BAD_REQUEST)
