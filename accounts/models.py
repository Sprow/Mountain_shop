from django.db import models

from django.contrib.auth.models import AbstractUser

from decimal import Decimal


class User(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal("0.00"))

    class Meta:
        swappable = 'AUTH_USER_MODEL'

