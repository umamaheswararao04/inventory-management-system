from django.db import models
 # Replace Product with your actual model
# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class StockHistory(models.Model):
    CHANGE_TYPES = (
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    change_type = models.CharField(max_length=3, choices=CHANGE_TYPES)
    quantity_changed = models.IntegerField()
    previous_quantity = models.IntegerField()
    new_quantity = models.IntegerField()
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.change_type}"
