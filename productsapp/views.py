from django.shortcuts import render
from .models import Supplier, Product

# Create your views here.
def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render (request,"suppliers.html",context)

def productlistview(request):
    productlist = Product.objects.all()
    context = {'products': productlist}
    return render (request,"products.html",context)

def addsupplier(request):
    newsupplier = request.POST['supplier']
    Supplier(supplier = newsupplier).save()
    return redirect(request.META['HTTP_REFERER'])