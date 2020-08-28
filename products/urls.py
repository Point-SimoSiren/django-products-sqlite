from django.contrib import admin
from django.urls import path,include
# includella liitetään itsetehdyn productsappin polut projektiin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('productsapp.urls'))
]
