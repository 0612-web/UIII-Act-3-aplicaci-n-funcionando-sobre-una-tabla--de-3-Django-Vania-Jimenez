from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

def inicio_Ventaropa(request):
    return render(request, 'inicio.html')

def agregar_producto(request):
    if request.method == 'POST':
        Producto.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            categoria=request.POST['categoria'],
            precio=request.POST['precio'],
            stock=request.POST['stock'],
            talla=request.POST['talla'],
            color=request.POST['color']
        )
        return redirect('ver_productos')
    return render(request, 'producto/agregar_producto.html')

def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/ver_productos.html', {'productos': productos})

def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'producto/actualizar_producto.html', {'producto': producto})

def realizar_actualizacion_producto(request, producto_id):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, id=producto_id)
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.categoria = request.POST['categoria']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.talla = request.POST['talla']
        producto.color = request.POST['color']
        producto.save()
        return redirect('ver_productos')
    return redirect('ver_productos')

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})