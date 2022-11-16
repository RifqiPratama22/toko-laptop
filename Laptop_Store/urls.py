from django.contrib import admin
from django.urls import path, include
from Laptop_Store.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('about', about, name='about'),
    path('barang/', include('barang.urls')),
]
