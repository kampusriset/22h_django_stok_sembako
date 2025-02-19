from django.contrib import admin
from django.urls import path, include

from stok_sembako import views

urlpatterns = [
    path('', views.index),
    path('tabel/', include('tabel_stok.urls')),
    path('admin/', admin.site.urls),
]
