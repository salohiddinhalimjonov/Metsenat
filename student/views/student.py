from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from student.models.student import Student
from student.serializers.student import StudentSerializer, StudentUpdateSerializer


class StudentViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    serializer_class = StudentSerializer
    filterset_fields = ['student_type', 'otm']
    search_fields = ['full_name']

    def get_queryset(self):
        return Student.objects.all()

    def update(self, request, *args, **kwargs):
        self.serializer_class = StudentUpdateSerializer
        return super(StudentViewSet, self).update(request, *args, **kwargs)
