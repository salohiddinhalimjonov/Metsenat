from django.db import models
from core.base_model import BaseModel
from sponsor.models.sponsor import Sponsor
from student.models.student import Student


class Payment(BaseModel):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.PROTECT, related_name='payments_of')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments_for')
    given_money = models.DecimalField(max_digits=21, decimal_places=2)

    def __str__(self):
        return self.given_money
