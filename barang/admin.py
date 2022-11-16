from django.contrib import admin
from barang.models import *
# Register your models here.
admin.site.register(Merek)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ['nama','deskripsi','harga']
admin.site.register(Produk, ProdukAdmin)
# Register your models here.
