from django.contrib import admin
from django.urls import path
from .views import supplierlistview, productlistview, addsupplier

urlpatterns = [
    path('', supplierlistview),
    path('addsupplier/',addsupplier),
    path('products/', productlistview)
]
