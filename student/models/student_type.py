from django.db import models
from core.base_model import BaseModel


class StudentType(BaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
