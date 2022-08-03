from django.contrib import admin
from sponsor.models.payment_type import PaymentType
from sponsor.models.sponsor import Sponsor
from sponsor.models.sponsor import Sponsor

# Register your models here.
admin.site.register([PaymentType, Sponsor])
