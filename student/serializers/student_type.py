from rest_framework import serializers
from student.models.student_type import StudentType


class StudentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentType
        fields = [
            'id',
            'name'
        ]
