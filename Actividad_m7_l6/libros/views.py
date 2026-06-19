from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_400_with_404
from .models import Libro
from .forms import LibroForm

# 1. Listar libros
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/listar_libros.html', {'libros': libros})

# 2. Crear libro
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_変更(): # o isValid
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/formulario_libro.html', {'form': form, 'accion': 'Crear'})

# 3. Editar libro
def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/formulario_libro.html', {'form': form, 'accion': 'Editar', 'libro': libro})

# 4. Eliminar libro
def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'libros/confirmar_eliminacion.html', {'libro': libro})