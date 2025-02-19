from django import forms
from .models import ProdukSembako
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
        
class FormProdukSembako(forms.ModelForm):
    class Meta:
        model = ProdukSembako
        fields = "__all__"
        
class FormDaftarAkun(UserCreationForm):
    password2= forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class FormChangePassword(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']