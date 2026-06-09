from utils import limpiar_pantalla, pausar, separador, pedir_entero

from productos import (
    cargar_catalogo,
    mostrar_catalogo,
    buscar_producto,
    actualizar_stock,
    registrar_producto
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

#Ejecuta el ciclo completo de una venta desde el carrito hasta el ticket
def proceso_venta(catalogo, numero_venta):
    carrito = crear_carrito()

    if not catalogo:
        print("El catalogo esta vacio. No se puede realizar venta")
        pausar()
        return False

    while True:
        limpiar_pantalla()
        print(f"\n Venta #{numero_venta:04d} | Productos en carrito: {len(carrito)}")
        opcion = mostrar_menu_venta()

        #Agregar producto
        if opcion == "1":
            limpiar_pantalla()
            mostrar_catalogo(catalogo)
            id = input(" Id del producto: ").strip().upper()
            cantidad = pedir_entero(" Cantidad: ", minimo=1)
            agregar_al_carrito(carrito, catalogo, id, cantidad)
            pausar()

        elif opcion == "2":
            limpiar_pantalla()
            eliminar_del_carrito(carrito)
            pausar()

        elif opcion == "3":
            limpiar_pantalla()
            mostrar_carrito(carrito)
            pausar()

        elif opcion =="4":
            if not carrito:
                print("No hay productos en el carrito")
                pausar()
                continue

            limpiar_pantalla()
            generar_ticket(carrito, numero_venta)

            confirmar = input("\n ¿Confirmar venta? (s/n): ").strip().lower()

            if confirmar == "s":
                for item in carrito:
                    actualizar_stock(catalogo, item["id"], item["cantidad"])
                guardar_venta(carrito, numero_venta)
                print("\n Venta registrada exitosamente, Gracias!")
                pausar()
                return True
            else:
                print("\n Venta no confirmada. Puedes seguir editando el carrito")
                pausar()

        elif opcion == "5":
            confirmar = input("\n ¿Estas seguro de cancelar la venta? (s/n)")
            if confirmar.lower() == "s":
                vaciar_carrito(carrito)
                print("\n Venta cancelada")
                pausar()
                return False
        else:
            print("\n Opcion no valida. Intenta de nuevo.")
            pausar()
def mostrar_menu_historial():
    separador("=")
    print("      SISTEMA POS - MENU HISTORIAL")
    separador("=")
    print("\n  1. Ver resumen de ventas")
    print("  2. Ver detalle de una venta")
    print("  3. Volver al menu principal")
    separador("=")
    return input("  Seleccione una opcion: ").strip()

def menu_historial():
    while True:
        limpiar_pantalla()
        opcion = mostrar_menu_historial()

        if opcion == "1":
            limpiar_pantalla()
            mostrar_historial()
            pausar()

        elif opcion == "2":
            limpiar_pantalla()
            mostrar_detalle_venta()
            pausar()

        elif opcion == "3":
            break
        
        else:
            print("\n Opcion no valida. Intenta de nuevo")
            pausar()

def main():
    catalogo = cargar_catalogo()
    numero_venta = obtener_numero_venta()

    while True:
        limpiar_pantalla()
        opcion = mostrar_menu_principal()

        # nueva venta
        if opcion == "1":
            venta_completada = proceso_venta(catalogo, numero_venta)
            if venta_completada:
                numero_venta += 1
            
        elif opcion == "2":
            limpiar_pantalla()
            mostrar_catalogo(catalogo)
            pausar()

        elif opcion == "3":
            limpiar_pantalla()
            registrar_producto(catalogo)
            pausar()

        elif opcion == "4":
            menu_historial()

        elif opcion == "5":
            limpiar_pantalla()
            print("\n Cerrando el sistema... Hasta luego!!\n")
            break

        else:
            print("\n Opcion no valida. Intenta de nuevo")
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