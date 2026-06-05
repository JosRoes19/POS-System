"""
utils.py - Utilidades generales del sistema POS
===============================================
Este modulo agrupa funciones de apoyo que se reutilizan 
en todos los demas modulos del sistema.

Funciones disponibles:
    - limpiar pantalla   : borrar el contenido de la terminal
    - pausar             : detiene le programa hasta que el usuario presione Enter
    - separador          : imprime una linea decorativa
    - pedir_entero       : solicita y valida un numero entero
    - pedir_flotante     : solicita y valida un numero decimal
    - pedir_texto        : solicita y valida una cadena de texto no vacia    
"""

import subprocess

def limpiar_pantalla():
    """ Limpiar la pantalla de la terminal"""
    '''subprocess.run(["cls"] if os.name == "nt" else ["clear"])'''

    cmd = 'cls' if subprocess.os.name == 'nt' else 'clear'
    try: 
        subprocess.run(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al limpiar la pantalla: {e}")

def pausar():
    """ Detiene la ejecución del programa hasta que el usuario presione Enter"""
    input("\nPresiona Enter para continuar...")

def separador(caracter="-", largo= 55):
    """ Imprime una linea decorativa"""
    print(caracter * largo)

def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Error: El valor debe ser mayor o igual a {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"Error: El valor debe ser menor o igual a {maximo}")
                continue
            return valor
        except ValueError:
            print("Error: Debes ingresar un número entero")

def pedir_flotante(mensaje, minimo= 0.0):
    """Solicita al usuario un numero decimal, validando que sea positivo si se especifica"""
    while True:
        try: 
            valor = float(input(mensaje))
            if valor < minimo:
                print(f"Error: El valor debe ser mayor o igual a {minimo}")
                continue
            return valor
        except ValueError:
            print("Error: Debes ingresar un número válido")
        
def pedir_texto(mensaje):
    """Solicita al usuario una cadena de texto no vacia"""
    while True:
        valor = input(mensaje).strip()
        if not valor: 
            print("Error: No puedes dejar este campo vacio")
            continue
        return valor    

