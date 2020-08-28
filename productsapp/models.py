from django.db import models

class ProductModel(models.Model):
    productname = models.CharField(max_length = 20),
    packagesize = models.CharField(max_length = 20),
    unitprice = models.Integerfield(),
    unitsinstock = models.IntegerField(),
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

class Supplier(models.Model):
    companyname = models.CharField(max_length = 50),
    contactname = models.CharField(max_length = 50),
    address = models.CharField(max_length = 100),
    phone = models.CharField(max_length = 20),
    email = models.CharField(max_length = 50),
    country = models.CharField(max_length = 20)

