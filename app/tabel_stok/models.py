from django.db import models

class ProdukSembako(models.Model):
    nama_produk = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField()
    kategori = models.CharField(max_length=100)
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama_produk
