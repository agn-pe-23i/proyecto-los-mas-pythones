# Definición de la estructura de datos para cada tipo de producto
import sys
import os
import time
import menu
import archivos

# Catálogo de productos
catalogo = None

def main():
    """
    Menú principal para visualizar y manipular el catálogo de productos
    """
    global catalogo
    opciones = list(map(str, range(1, 8)))

    while True:
        print("Menú principal:\n")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Eliminar producto")
        print("4. Mostrar catálogo")
        print("5. Cargar catálogo desde archivo")
        print("6. Guardar catálogo en archivo")
        print("7. Salir\n")
            
        opcion = input("Seleccione una opción: ")

        if opcion in opciones:
            menu.espera()
            if opcion == "1":
                catalogo = menu.agregar_producto(catalogo)
            elif opcion == "2":
                menu.buscar_producto(catalogo)
            elif opcion == "3":
                menu.eliminar_producto(catalogo)
            elif opcion == "4":
                menu.mostrar_catalogo(catalogo)
            elif opcion == "5":
                catalogo = archivos.cargar_catalogo()
            elif opcion == "6":
                archivos.guardar_catalogo(catalogo)
            elif opcion == "7":
                print('Saliendo del programa. . .')
                menu.espera()
                sys.exit(0)
        else:
            print("\nOpción inválida. Por favor, seleccione una opción válida.")
            menu.continuar()

main()