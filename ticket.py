import json
import os
from datetime import datetime

from utils import separador, pausar
from ventas import calcular_totales

# Ruta del archivo donde se guarda el historial de ventas
ARCHIVO_HISTORIAL  = os.path.join("datos", "historial_ventas.json")

# Historial
def cargar_historial():
    if os.path.exists(ARCHIVO_HISTORIAL):
        with open(ARCHIVO_HISTORIAL, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    return []

def guardar_venta(carrito, numero_venta):
    subtotal, iva, total = calcular_totales(carrito)
    fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    productos_historial = []
    for item in carrito:
        productos_historial.append({
            "codigo": item["id"],
            "nombre": item["nombre"],
            "precio": item["precio"],
            "cantidad": item["cantidad"],
            "subtotal": item["subtotal"]
        })

    venta = {
        "numero": numero_venta,
        "fecha": fecha_hora,
        "productos": productos_historial,
        "subtotal": subtotal,
        "iva": iva,
        "total": total
    }

    historial = cargar_historial()
    historial.append(venta)

    os.makedirs("datos", exist_ok=True)
    with open(ARCHIVO_HISTORIAL, "w", encoding="utf-8") as archivo:
        json.dump(historial, archivo, indent=4, ensure_ascii=False)

# Determina el numero correlativo de la proxuma venta
""" Ejemplo de salida
    ==================================================
            SISTEMA POS - TICKET DE VENTA
    ==================================================
    Venta #: 1
    Fecha: 06/06/2026   Hora: 12:34:56
    --------------------------------------------------
    Producto         Cantidad   Precio-Unit    Total
    --------------------------------------------------
    Laptop-Apple-M3   1         $1000.00      $1000.00
    Mouse-Logitech     1         $50.00         $50.00
    --------------------------------------------------
    Subtotal:                                 $1050.00
    IVA (16%):                                 $168.00
    --------------------------------------------------
    Total:                                    $1218.00
    Gracias por su compra.
    ==================================================
    """

def obtener_numero_venta():
    historial = cargar_historial()
    if not historial:
        return 1
    last_sale = historial[-1]
    if 'numero' in last_sale:
        return last_sale['numero'] + 1
    elif 'id' in last_sale:
        return last_sale['id'] + 1
    return len(historial) + 1

numero = obtener_numero_venta()

def generar_ticket(carrito, numero_venta):
    subtotal, iva, total = calcular_totales(carrito)
    fecha_hora = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")

    if not carrito:
        print("\n No hay productos en el carrito para generar un ticket.")
        return False
    else:
        separador("=")
        print("SISTEMA POS - TICKET DE VENTA")
        separador("=")
        print(f"Venta #: {numero_venta}")
        print(f"Fecha: {fecha_hora}")
        separador("-")
        print(
            f"{ 'Producto': <26} { 'Cantidad': >4}"
            f"{ 'Precio-Unit': >9} {'Total': >10}"
        )

        separador()
        print(f"{'Subtotal': >38} ${subtotal:>9.2f}")
        print(f"{'IVA (16%)': >38} ${iva:>9.2f}")
        separador()
        print(f"{'Total': >38} ${total:>9.2f}")
        separador("=")
        print("Gracias por su compra.")
        separador("=")

        return subtotal, iva, total

# Historial en pantalla
""" Ejemplo de salida:
    ===========================================================
                    Historial de ventas
    ===========================================================
    #       Fecha               Productos               Total
    -----------------------------------------------------------
    #1  27/04/2026 10:35:03         3                  $1200.20   
"""

def mostrar_historial():
    historial = cargar_historial()

    if not historial:
        print("\n   No hay ventas registradas en el historial.")
    else:
        separador("=")
        print("     Historial de ventas")
        separador("=")
        print(f"    {'#':<6} {'Fecha':<20} {'Productos':<10} {'Total':<10}")
        separador()
        for venta in historial:
            items_list = venta.get("productos") or venta.get("items") or []
            num_productos = sum(p.get("cantidad", 0) for p in items_list)
            sale_num = venta.get("numero") or venta.get("id") or 0
            print(
                f"  #{sale_num:<5} {venta['fecha']}"
                f" {num_productos: <10}" f" ${venta['total']: >11.2f}"
            )
        separador()

# Muestra el detalle completo de una venta seleccionada por el usuario
""" Ejemplo de salida: 
        ===========================================================
                    Detalle de Venta #1
        ===========================================================
        Producto                            Cantidad   Precio-Unit    Total
        -----------------------------------------------------------
        Laptop-Apple-M3                              1    $1000.00   $1000.00
        Mouse-Logitech                               1      $50.00     $50.00
        -----------------------------------------------------------
        Subtotal:                                           $1050.00
        IVA (16%):                                           $168.00
        -----------------------------------------------------------
        Total:                                           $1218.00
        ===========================================================
"""

def mostrar_detalle_venta(numero_venta):
    historial = cargar_historial()

    if not historial:
        print("\n  No hay ventas registradas en el historial.")
        return

    mostrar_historial()
    numero = input("\n  Ingrese el número de venta a consultar o 0 para cancelar: ").strip()

    if numero == '0':
        return

    try:
        numero = int(numero)
    except ValueError:
        print("\n Entrada no valida.")
        return

    # Busca la venta por numero
    venta = next((v for v in historial if (v.get('id') == numero or v.get('numero') == numero)), None)

    if venta is None:
        print(f"\n No se encontro venta con numero #{numero}")
        return

    separador("=")
    sale_num = venta.get("numero") or venta.get("id") or 0
    print(f"            Detalle de Venta #{sale_num}")
    separador("=")
    print(f"{'Producto':<30} {'Cantidad':<10} {'Precio-Unit':<12} {'Total':<10}")
    separador("-")
    items_list = venta.get("productos") or venta.get("items") or []
    for item in items_list:
        name = item.get('nombre', '')
        qty = item.get('cantidad', 0)
        price = item.get('precio', 0.0)
        subt = item.get('subtotal', 0.0)
        print(
            f"{name:<30} {qty:<10} "
            f"${price:<11.2f} ${subt:<10.2f}"
        )
    separador("-")
    print(f"{'Subtotal:':<53} ${venta['subtotal']:>8.2f}")
    print(f"{'IVA (16%):':<53} ${venta['iva']:>8.2f}")
    separador("-")
    print(f"{'Total:':<53} ${venta['total']:>8.2f}")
    separador("=")
    pausar()