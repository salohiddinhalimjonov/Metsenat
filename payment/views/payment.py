from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from payment.models.payment import Payment
from student.models.student import Student
from sponsor.models.sponsor import Sponsor
from payment.serializers.payment import PaymentSerializer
from payment.services.create_or_update_payment import create_or_update_payment, update


class PaymentViewSet(GenericViewSet):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.exclude(sponsor__sponsor_type=Sponsor.BEKOR)

    def create(self, request):
        student_id = request.query_params.get('student_id')
        student = get_object_or_404(Student, id=student_id)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return create_or_update_payment(student, serializer)

    def update(self, request, *args, **kwargs):
        student_id = request.query_params.get('student_id')
        student = get_object_or_404(Student, id=student_id)
        obj = self.get_object()
        serializer = self.serializer_class(instance=obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        return update(student, serializer)

    def list(self, request):
        student_id = request.query_params.get('student_id')
        student = get_object_or_404(Student, id=student_id)
        queryset = Payment.objects.filter(student=student)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, *args, **kwargs):
        obj = self.get_object()
        sponsor = obj.sponsor
        sponsor.payment_amount += obj.given_money
        sponsor.save(update_fields=['payment_amount'])
        obj.delete()
        return Response({'detail': 'Payment object has benn deleted!'}, status=status.HTTP_204_NO_CONTENT)
