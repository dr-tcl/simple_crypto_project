from django.db import models
from utils.model import BaseModel


class OrderQueue(BaseModel):
    crypto_name = models.CharField(max_length=255,unique=True)
    total_amount = models.PositiveIntegerField()
    orders = models.ManyToManyField('user.Order')
    paid_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.crypto_name
