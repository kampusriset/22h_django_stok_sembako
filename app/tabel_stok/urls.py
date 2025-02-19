from django.urls import path

from . import views 

urlpatterns = [
    path('', views.tabel),
    path('tambah/', views.tambah),
    path('update/<int:id>/', views.update),
    path('hapus/<int:id>/', views.hapus),
    path('login/', views.user_login),
    path('daftar/', views.user_daftar),
    path('logout/', views.user_logout),
    path('ubah_pw/', views.ganti_password),
]