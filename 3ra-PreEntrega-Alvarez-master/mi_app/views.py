from django.shortcuts import render, redirect
from .models import *
from .forms import *
import os
from django.conf import settings

def inicio(request):
    print(os.path.join(settings.BASE_DIR, 'mi_app', 'templates', 'inicio.html'))
    return render(request, 'inicio.html')


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_producto')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def buscar_producto(request):
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        productos = Producto.objects.filter(nombre__icontains=nombre)
    else:
        productos = Producto.objects.all()
    return render(request, 'buscar_producto.html', {'productos': productos})
