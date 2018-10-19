from django.db import models


class ExchangeRate(models.Model):
    currency = models.CharField(max_length=3)
    value = models.DecimalField(decimal_places=4, max_digits=12)
    updated = models.DateTimeField()

