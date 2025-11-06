from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_Ventaropa, name='inicio'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('ver-productos/', views.ver_productos, name='ver_productos'),
    path('actualizar-producto/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),
    path('realizar-actualizacion/<int:producto_id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('borrar-producto/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
]