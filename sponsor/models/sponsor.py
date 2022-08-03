from django.db import models
from core.base_model import BaseModel
from sponsor.models.payment_type import PaymentType


class Sponsor(BaseModel):

    YANGI = "YANGI"
    TASDIQLANGAN = "TASDIQLANGAN"
    BEKOR = "BEKOR QILINGAN"
    MODERATSIYADA = "MODERATSIYADA"

    SPONSOR_STATUS = (
        (YANGI, YANGI),
        (TASDIQLANGAN, TASDIQLANGAN),
        (BEKOR, BEKOR),
        (MODERATSIYADA, MODERATSIYADA)
    )

    sponsor_type = models.CharField(max_length=64)
    sponsor_status = models.CharField(max_length=32, choices=SPONSOR_STATUS, default=YANGI)
    full_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)
    payment_amount = models.DecimalField(max_digits=21, decimal_places=2)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT, related_name='sponsors', null=True)
    organization = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.full_name
