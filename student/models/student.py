from django.db import models
from core.base_model import BaseModel
from student.models.otm import OTM
from student.models.student_type import StudentType


class Student(BaseModel):
    full_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)
    otm = models.ForeignKey(OTM, on_delete=models.PROTECT)
    student_type = models.ForeignKey(StudentType, on_delete=models.PROTECT)
    tuition_fee = models.DecimalField(max_digits=21, decimal_places=2)

    def __str__(self):
        return self.full_name
