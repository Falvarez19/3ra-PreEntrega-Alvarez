from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'categoria', 'disponible']

class BuscarProductoForm(forms.Form):
    nombre = forms.CharField(label='Buscar por nombre', max_length=100)
