#Django core 
from django.db import models

# Apps model import
from apps.authentication.models import CustomUsers
from apps.base.base_model import BaseModel

class Transaction(BaseModel):
    made_by = models.ForeignKey(CustomUsers, on_delete=models.CASCADE )
    # made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.created_at and self.id:
            self.order_id = self.created_at.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)
