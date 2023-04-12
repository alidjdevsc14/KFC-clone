from django.db import models
from django.utils.datetime_safe import datetime

from accounts.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Category'


class SubCategory(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category2 = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sub Category'


class Item(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    # sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, default=None, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    pre_item = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.name)


    class Meta:
        verbose_name_plural = 'Item'


class Orders(models.Model):
    PICKUP = 1
    DELIVERY = 2
    DELIVERY_CHOICES = (
        (PICKUP, 'Pick-up'),
        (DELIVERY, 'Delivery'),
    )
    is_pickup = models.IntegerField(choices=DELIVERY_CHOICES)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    pre_order = models.BooleanField(default=False)
    name = models.CharField(max_length=50, default='', blank=True)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.item)

    class Meta:
        verbose_name_plural = 'Orders'
