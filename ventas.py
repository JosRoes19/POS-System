from utils import separador
from productos import buscar_producto

TASA_IVA = 0.16 

def crear_carrito():
    return[]

# Agregar un producto al carrito, verificando su disponibilidad en el catalogo
def agregar_al_carrito(carrito, catalogo, id, cantidad):
    producto = buscar_producto(catalogo, id)

    if producto is None:
        print(f"Producto con ID {id} no existe en el catalogo.")
        return False

# Calcular cuantas unidades ya estan en el carrito de este producto
    cantidad_en_carrito = 0

    for item in carrito:
        if item['id'] == id.upper():
            cantidad_en_carrito = item['cantidad']
            break

    if producto['stock'] < cantidad + cantidad_en_carrito:
        disponible = producto['stock'] - cantidad_en_carrito
        print(f"\n  Stock insuficiente. Puedes agregar hasta {disponible} unidad(es).")
        return False

# Si el producto ya esta en el carrito, actualizamos la cantidad
    for item in carrito:
        if item['id'] == id.upper():
            item['cantidad'] += cantidad
            item['subtotal'] = item['cantidad'] * item['precio']
            print(f"\n  Se han agregado {cantidad} unidades mas al producto {producto['nombre']}.")
            return True

# Si el producto no esta en el carrito, lo agregamos
    nuevo_item = {
        'id': producto['id'],
        'nombre': producto['nombre'],
        'precio': producto['precio'],
        'cantidad': cantidad,
        'subtotal': producto['precio'] * cantidad,
    }
    carrito.append(nuevo_item)
    print(f"\n  Se ha agregado {cantidad} unidad(es) del producto {producto['nombre']}.")
    return True

# Permite al usuario seleccionar y eliminar un producto del carrito
def eliminar_del_carrito(carrito):
    if not carrito:
        print("\n  El carrito esta vacio. No hay productos para eliminar.")
        return
    
    mostrar_carrito(carrito)
    numero = input(" Numero del producto a eliminar (0 oara cancelar): ").strip()

    if numero == '0':
        print("\n  Operacion cancelada.")
        return

    try:
        indice = int(numero) - 1
        if 0 <= indice < len(carrito):
            nombre = carrito[indice]['nombre']
            carrito.pop(indice)
            print(f"\n  Producto {nombre} eliminado del carrito.")
        else:
            print("\n  Numero de producto invalido.")
    except ValueError:
        print("\n  Entrada invalida. Por favor, ingrese un numero.")

def mostrar_carrito(carrito):
    if not carrito:
        print("\n  El carrito esta vacio.")
    else:
        separador("=")
        print(f"    CARRITO DE COMPRA")
        separador("=")

        print(f"    {'No.':<3} {'Producto':<20} {'Cant':<5} {'Precio':<10} {'Subtotal':<10}")
        separador("=")

        for i, item in enumerate(carrito, start=1):
            print(f"    {i:<4} {item['nombre']:<26}"
            f"{item['cantidad']:<5} "
            f"{item['precio']:<10.2f} {item['subtotal']:<10.2f}")
        separador("=")

def calcular_totales(carrito):
    subtotal = sum(item["subtotal"] for item in carrito)
    iva = subtotal * TASA_IVA
    total = subtotal + iva
    return subtotal, iva, total

def vaciar_carrito(carrito):
    carrito.clear()
    print("\n  Carrito vaciado.")