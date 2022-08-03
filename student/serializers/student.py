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
            # ajratilgan pul
        ]


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
