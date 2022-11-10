#Django core 
from django.db import models

# Apps model import
from apps.authentication.models import CustomUsers
from apps.base.base_model import BaseModel

class Transaction(BaseModel):
    made_by = models.ForeignKey(CustomUsers, on_delete=models.CASCADE )
    # made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(null=True, blank=True)
    # order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    paid = models.BooleanField(default=False)
    # checksum = models.CharField(max_length=100, null=True, blank=True)
    