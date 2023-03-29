from django.db import models


class Payment(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=64)
    amount = models.PositiveBigIntegerField()
    description = models.TextField()
