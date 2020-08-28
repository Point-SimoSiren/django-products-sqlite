from django.shortcuts import render,redirect
from .models import Supplier, Product

def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render (request,"suppliers.html",context)

def addsupplier(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])

def deletesupplier(request,iidee):
    Supplier.objects.filter(id = iidee).delete()
    return redirect(request.META['HTTP_REFERER'])

def productlistview(request):
    productlist = Product.objects.all()
    context = {'products': productlist}
    return render (request,"products.html",context)

  