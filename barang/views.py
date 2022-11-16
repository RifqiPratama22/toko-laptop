from django.shortcuts import redirect, render
from barang.models import Merek, Produk
# Create your views here.
def barang_list(request):
    template_name = 'barang_list.html'
    produk_list = Produk.objects.all()
    context = {
        'title' :'Laptop Store',
        'produk': produk_list
    }
    return render(request, template_name, context)

def barang_add(request):
    template_name = 'barang_add.html'
    merek = Merek.objects.all()
    if request.method == "POST":
        input_merek = request.POST.get('merek')
        input_nama = request.POST.get('nama')
        input_deskripsi = request.POST.get('deskripsi')
        input_harga = request.POST.get('harga')

        # memanggil Jenis
        get_merek = Merek.objects.get(nama=input_merek)
        
        #simpan produk karena ada relasi ke tabel Jenis
        Produk.objects.create(
            nama = input_nama,
            deskripsi = input_deskripsi,
            harga = input_harga,
            merek = get_merek,
        )
        return redirect(barang_list)

        
    context = {
        'title' :'tambah barang',
        'merek':merek
        
    }
    return render(request, template_name, context)

def barang_update(request, id):
    template_name = 'barang_add.html'
    merek = Merek.objects.all()
    get_produk = Produk.objects.get(id=id)

    if request.method == "POST":
        input_merek = request.POST.get('merek')
        input_nama = request.POST.get('nama')
        input_deskripsi = request.POST.get('deskripsi')
        input_harga = request.POST.get('harga')

        # memanggil Jenis
        get_merek = Merek.objects.get(nama=input_merek)
        
        #simpan produk karena ada relasi ke tabel Jenis
        get_produk.nama = input_nama
        get_produk.deskripsi = input_deskripsi
        get_produk.harga = input_harga
        get_produk.merek = get_merek
        get_produk.save()
        return redirect(barang_list)
    context = {
        'title' :'tambah barang',
        'merek':merek,
        'get_produk':get_produk,
        
    }
    return render(request, template_name, context)

def barang_delete(request, id):
    produk = Produk.objects.get(id=id).delete()
    return redirect(barang_list)