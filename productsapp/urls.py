from django.contrib import admin
from django.urls import path
from .views import supplierlistview, productlistview

urlpatterns = [
    path('', supplierlistview),
    path('products/', productlistview)
]
