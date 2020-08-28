from django.contrib import admin
from django.urls import path
from .views import supplierlistview, productlistview, addsupplier, deletesupplier

urlpatterns = [
    path('', supplierlistview),
    path('addsupplier/',addsupplier),
    path('deletesupplier/<int:iidee>/',deletesupplier),
    path('products/', productlistview),

]
