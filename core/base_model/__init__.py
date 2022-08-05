from django.db import models


class BaseModel(models.Model):
    created_datetime = models.DateField(auto_now_add=True)
    modified_datetime = models.DateField(auto_now=True)

    class Meta:
        abstract = True
