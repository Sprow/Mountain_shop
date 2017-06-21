from django.db import models

from products.models import Product


class Cart(models.Model):
    full_cart = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', null=True, blank=True)
    item = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField(default=1)
    item_total_price = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)



