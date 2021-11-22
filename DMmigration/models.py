from django.db import models

# Create your models here.

class OrderDetail(models.Model):
    OrderId = models.CharField(max_length=50)
    ProductId = models.CharField(max_length=50)
    UnitPrice = models.CharField(max_length=100)
    Quantity = models.CharField(max_length=100)
