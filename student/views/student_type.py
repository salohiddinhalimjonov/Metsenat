from rest_framework.viewsets import ModelViewSet
from student.serializers.student_type import StudentTypeSerializer
from student.models.student_type import StudentType


class StudentTypeViewSet(ModelViewSet):
    serializer_class = StudentTypeSerializer

    def get_queryset(self):
        return StudentType.objects.all()
