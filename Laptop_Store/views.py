from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    context = {
        'title' :'Selamat datang di Toko Laptop'
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'about.html'
    context = {
        'title' :'Tentang Toko Laptop'
    }
    return render(request, template_name, context)
