import json
import os
from utils import pedir_entero, pedir_flotante, pedir_texto, separador

#Ruta del archivo donde se guarda el catalogo

ARCHIVO_CATALOGO = os.path.join("datos", "catalogo.json")

CATALAGO_INICIAL = {
    "A001": {"nombre": "Laptop Dell XPS 15", "precio": 1899.99, "stock": 10},
    "A002": {"nombre": "Smartphone Samsung Galaxy S23", "precio": 799.99, "stock": 15},
    "B003": {"nombre": "Mouse Logitech MX Master 3", "precio": 99.99, "stock": 20},
    "C004": {"nombre": "Teclado Mecanico Redragon K552", "precio": 59.99, "stock": 25},
    "D005": {"nombre": "Monitor LG 24GL600F", "precio": 199.99, "stock": 30},
    "E006": {"nombre": "Webcam Logitech C920", "precio": 79.99, "stock": 35},
    "F007": {"nombre": "Audifonos HyperX Cloud II", "precio": 99.99, "stock": 40},
    "G008": {"nombre": "Microfono Blue Yeti", "precio": 129.99, "stock": 45},
}

""" Carga el catalogo de productos desde el archivo JSON. Si no existe, crea uno nuevo """
def cargar_catalogo():
    if os.path.exists(ARCHIVO_CATALOGO):
        with open(ARCHIVO_CATALOGO, "r", encoding='utf-8') as archivo:
            return json.load(archivo)
    return CATALAGO_INICIAL.copy()

# Guardar el catalogo en el archivo JSON
def guardar_catalogo(catalogo):
    with open(ARCHIVO_CATALOGO, "w", encoding='utf-8') as archivo:
        json.dump(catalogo, archivo, indent=4, ensure_ascii=False)

#Muesta el catalogo de productos en pantalla
def mostrar_catalogo(catalogo):
    separador("=")
    print("                 \n CATÁLOGO DE PRODUCTOS:\n")
    separador("=")

    if not catalogo:
        print("\n  No hay productos registrados.")
    else: 
        print(f" {'ID':<6} {'NOMBRE':<30} {'PRECIO':<10} {'STOCK':<6}")
        separador("=")
        for id, producto in catalogo.items():
            print(
                f" {id:<6} {producto['nombre']:<30} "
                f"${producto['precio']:<9.2f} {producto['stock']:<6}"
                )

    separador("=")

def buscar_producto(catalogo, id):
    return catalogo.get(id.upper())

#Agrega un nuevo producto al catalogo
def registrar_producto(catalogo):
    separador("=")
    print("                  AGREGAR NUEVO PRODUCTO")
    separador("=")

    id = pedir_texto("\n Ingrese el ID: ").upper()
    
    if id in catalogo:
        print(f"\n El producto con ID '{id}' ya existe.")
        return

    nombre = pedir_texto("\n Ingrese el nombre: ")
    precio = pedir_flotante("\n Ingrese el precio: ")
    stock = pedir_entero("\n Ingrese el stock: ")

    catalogo[id] = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    guardar_catalogo(catalogo)
    print(f"\n¡Producto '{nombre}' con ID '{id}' registrado exitosamente!")

def actualizar_stock(catalogo, id, cantidad_vendida):
    if id in catalogo:
        catalogo[id]['stock'] -= cantidad_vendida
        guardar_catalogo(catalogo)
        