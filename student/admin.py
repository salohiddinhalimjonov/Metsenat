from django.contrib import admin
from student.models.otm import OTM
from student.models.student import Student
from student.models.student_type import StudentType

admin.site.register([OTM, Student, StudentType])
