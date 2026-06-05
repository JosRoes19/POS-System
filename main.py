from utils import limpiar_pantalla, pausar, separador, pedir_entero

from productos import (
    cargar_catalogo,
    mostrar_catalogo,
    buscar_producto,
    actualizar_stock
)

from ventas import (
    crear_carrito,
    agregar_al_carrito,
    eliminar_del_carrito,
    mostrar_carrito,
    vaciar_carrito
)

from ticket import (
    generar_ticket,
    guardar_venta,
    obtener_numero_venta,
    mostrar_historial,
    mostrar_detalle_venta
)

# Menus
# Imprime el menu principal del sustema y solicita una opcion al usuario
def mostrar_menu_principal():
    separador("=")
    print("        SISTEMA POS - MENU PRINCIPAL")
    separador("=")
    print("\n  1. Nueva venta")
    print("  2. Ver catalogo de productos")
    print("  3. Agregar producto al catalogo")
    print("  4. Historial de ventas")
    print("  5. Salir")
    separador("=")
    return input("\n  Seleccione una opcion: ").strip()

# Imprimeel menu de opciones durante una venta activa y solicita una opcion al usuario
def mostrar_menu_venta():
    separador("=")
    print(" Menu de venta")
    separador("=")
    print("\n  1. Agregar producto al carrito")
    print("  2. Eliminar producto del carrito")
    print("  3. Ver carrito")
    print("  4. Finalizar venta")
    print("  5. Cancelar venta")
    separador("=")
    return input("  Seleccione una opcion: ").strip()

def main():
    catalogo = cargar_catalogo()

    while True:
        limpiar_pantalla()
        opcion = mostrar_menu_principal()

        if opcion == "1":
            # Nueva venta
            carrito = crear_carrito()
            numero_venta = obtener_numero_venta()
            while True:
                limpiar_pantalla()
                print(f"\n  === VENTA ACTIVA #{numero_venta} ===")
                mostrar_carrito(carrito)
                opcion_venta = mostrar_menu_venta()

                if opcion_venta == "1":
                    # Agregar producto al carrito
                    limpiar_pantalla()
                    mostrar_catalogo(catalogo)
                    id_prod = pedir_texto("\n  Ingrese el ID del producto: ").upper()
                    producto = buscar_producto(catalogo, id_prod)
                    if producto:
                        cant = pedir_entero("  Ingrese la cantidad: ", minimo=1)
                        agregar_al_carrito(carrito, catalogo, id_prod, cant)
                    else:
                        print(f"\n  Producto con ID '{id_prod}' no encontrado.")
                    pausar()

                elif opcion_venta == "2":
                    # Eliminar producto del carrito
                    limpiar_pantalla()
                    eliminar_del_carrito(carrito)
                    pausar()

                elif opcion_venta == "3":
                    # Ver carrito
                    limpiar_pantalla()
                    mostrar_carrito(carrito)
                    pausar()

                elif opcion_venta == "4":
                    # Finalizar venta
                    if not carrito:
                        print("\n  El carrito está vacío. No se puede finalizar la venta.")
                        pausar()
                        continue
                    
                    limpiar_pantalla()
                    generar_ticket(carrito, numero_venta)
                    
                    # Guardar venta en el historial
                    guardar_venta(carrito, numero_venta)
                    
                    # Actualizar stock de los productos vendidos
                    for item in carrito:
                        actualizar_stock(catalogo, item['id'], item['cantidad'])
                    
                    print("\n  Venta finalizada exitosamente.")
                    pausar()
                    break

                elif opcion_venta == "5":
                    # Cancelar venta
                    confirmar = pedir_texto("\n  ¿Está seguro que desea cancelar la venta? (s/n): ").lower()
                    if confirmar == 's':
                        vaciar_carrito(carrito)
                        print("\n  Venta cancelada.")
                        pausar()
                        break
                else:
                    print("\n  Opción no válida.")
                    pausar()

        elif opcion == "2":
            # Ver catalogo de productos
            limpiar_pantalla()
            mostrar_catalogo(catalogo)
            pausar()

        elif opcion == "3":
            # Agregar producto al catalogo
            limpiar_pantalla()
            registrar_producto(catalogo)
            pausar()

        elif opcion == "4":
            # Historial de ventas
            limpiar_pantalla()
            mostrar_detalle_venta(None)

        elif opcion == "5":
            # Salir
            print("\n  ¡Gracias por usar el sistema POS! Saliendo...")
            break
        else:
            print("\n  Opción no válida.")
            pausar()

# Este bloque asegura que main() solo se ejecute cuando se corre
# este archivo directamente
if __name__ == "__main__":
    main()



# funciones deflujo

"""# def start(): -> funcion encargada de iniciar el programa
def start():
    return None

# def update(): -> funcion encargada de actualizar el programa
def update():
    return None

# def new_sale(): -> funcion encargada de renderizar la interfaz del programa
def render():
    return None

# def destroy(): -> funcion encargada de cerrar el programa
def destroy():
    return None

# def run(): -> funcion encargada de ejecutar el programa
def run():
    start()
    while msg := mostrar_menu_principal()
        render()
        update()
    destroy()"""