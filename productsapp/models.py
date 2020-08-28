from django.db import models

class Supplier(models.Model):
    companyname = models.CharField(max_length = 50, default = 'lakufirma')
    contactname = models.CharField(max_length = 50, default = 'tommi')
    address = models.CharField(max_length = 100, default = 'trueflasecdo 3')
    phone = models.CharField(max_length = 20, default = '437483434')
    email = models.CharField(max_length = 50, default = 'vfgvvgfgfdv')
    country = models.CharField(max_length = 20, default = 'vdfvvbg')

class Product(models.Model):
    productname = models.CharField(max_length = 20, default = "laku")
    packagesize = models.CharField(max_length = 20, default = 3)
    unitprice = models.IntegerField(default = 3)
    unitsinstock = models.IntegerField(default = 3)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, default = 1)

