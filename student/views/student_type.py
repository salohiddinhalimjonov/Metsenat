from rest_framework.viewsets import ModelViewSet
from student.models.otm import OTM
from student.serializers.student_type import StudentType


class StudentTypeViewSet(ModelViewSet):
    serializer_class = StudentType

    def get_queryset(self):
        return StudentType.objects.all()
