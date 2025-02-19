from django.shortcuts import render,redirect,get_object_or_404
from tabel_stok.forms import FormProdukSembako, FormDaftarAkun, FormChangePassword
from .models import ProdukSembako
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.core.paginator import Paginator

def tabel(request):
    search = request.GET.get('search')
    data = ProdukSembako.objects.all()
    paginasi = Paginator(data, 3)  
    no_page = request.GET.get('hal')
    hal_paginasi = paginasi.get_page(no_page)
    if search:
        hal_paginasi = data.filter(
            Q(nama_produk__icontains=search) | Q(harga__icontains=search)| Q(stok__icontains=search) | Q(kategori__icontains=search)
        )
    
    context = {
        'data': hal_paginasi
    }
    return render(request, 'tabel_stok/tabel.html', context)

def tambah(request):
    if request.method == 'POST':
        form = FormProdukSembako(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/tabel') 
    else:
        form = FormProdukSembako()
        
    context = {
        'form': form
    }
    return render(request, 'tabel_stok/form_tambah.html',context)

def update(request, id):
    data = get_object_or_404(ProdukSembako, id=id)

    if request.method == 'POST':
    
        data.nama_produk = request.POST['nama_produk']
        data.harga = request.POST['harga']
        data.stok = request.POST['stok']
        data.kategori = request.POST['kategori']
        data.save()  

        return redirect('/tabel') 
    
    context = {
        'data': data
    }
    return render(request, 'tabel_stok/form_update.html', context)

def hapus(request,id):
    ProdukSembako.objects.filter(id=id).delete()
    return redirect('/tabel')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/') 
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Username atau password salah.'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_daftar(request):
    if request.method == 'POST':
        form = FormDaftarAkun(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/')  
        else:
            return render(request, 'daftar.html', {'form': form, 'error': 'Gagal daftar. Periksa inputan Anda.'})
    else:
        form = FormDaftarAkun()
    return render(request, 'daftar.html', {'form': form})

def user_logout(request):
    if request.method == 'POST':
        logout(request) 
        return redirect('/')  
    return render(request, 'logout.html')

def ganti_password(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        post = FormChangePassword(request.user, request.POST)
        if post.is_valid():
            post.save()
            return redirect('/')
        else:
            return render(request, 'form_change_pw.html', {'post': post, 'error': 'Gagal Ubah Password. Periksa inputan Anda.'})
    else:
        post = FormChangePassword(request.user)
    context = {
        'post': post,
    }
    return render(request, 'form_change_pw.html',context)