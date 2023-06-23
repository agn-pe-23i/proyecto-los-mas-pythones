import time
import os

def espera():
    """
    Realiza una pausa de 1 segundo y luego limpia la pantalla.
    Utiliza la función time.sleep() para generar la pausa y la función os.system()
    para limpiar la pantalla, utilizando comandos específicos dependiendo del sistema operativo.
    """
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

def continuar():
    """
    Pausa el programa y muestra un mensaje indicando al usuario que presione Enter para continuar.
    Luego, limpia la pantalla.
    Utiliza la función input() para esperar a que el usuario presione Enter y la función os.system()
    para limpiar la pantalla, utilizando comandos específicos dependiendo del sistema operativo.
    """
    input('\nPresione Enter para continuar. . .')
    os.system('cls' if os.name == 'nt' else 'clear')

def datosProducto(opcion):
    """
    Devuelve los datos requeridos para un tipo de producto específico.
    Recibe como parámetro la opción seleccionada por el usuario y devuelve una lista con los datos requeridos
    para el tipo de producto seleccionado.
    """
    datos = {
        'Película': ['Título', 'Actor principal', 'Director', 'Año', 'Precio de renta', 'Precio de venta'],
        'Serie': ['Título', 'Actor principal', 'Director', 'Temporadas', 'Precio de renta', 'Precio de venta'],
        'Documental': ['Título', 'Actor principal', 'Director', 'Tema', 'Año', 'Precio de renta', 'Precio de venta'],
        'Evento deportivo en vivo': ['Título', 'Deporte', 'Fecha', 'Hora', 'Lugar', 'Precio de venta']
    }

    return datos[opcion]

def agregar_producto(catalogo):
    """
    Permite agregar un producto al catálogo.
    Solicita al usuario la información correspondiente y crea una instancia
    del tipo de producto seleccionado para luego agregarlo al catálogo.
    """
    while True:
        print("¿Qué desea agregar?:\n")
        print("1. Película")
        print("2. Serie")
        print("3. Documental")
        print("4. Evento deportivo en vivo")
        print("5. Regresar\n")

        opciones = {'1': 'Película', '2': 'Serie', '3': 'Documental', '4': 'Evento deportivo en vivo'}
        opcion = input("Seleccione una opción: ")

        if opcion in opciones.keys():
            espera()
            producto = {}
            
            tipo = opciones[opcion]
            print(f'Ingresando {tipo}:\n')

            datos = datosProducto(tipo)
            producto['Tipo'] = tipo

            for dato in datos:
                dat = input(f'Ingrese {dato.lower()}: ' )
                producto[dato] = dat

            if catalogo is None:
                catalogo = []
               
            catalogo.append(producto)
            print(f'\n{tipo} agregado exitosamente')
            continuar()

        elif opcion == "5":
            print('\nRegresando al menú principal. . .')
            espera()
            return catalogo
        else:
            print("\nOpción inválida. Por favor, seleccione una opción válida.")
            continuar()

def buscar_producto(catalogo):
    """
    Permite buscar productos en el catálogo utilizando palabras clave del título.
    Solicita al usuario ingresar las palabras clave y muestra los productos encontrados.
    """
    if catalogo is None:
        print('No existe un catálogo.')
        continuar()
        return
    
    clave = input("Ingrese palabras clave del título del producto: ")
    productos_encontrados = []

    for producto in catalogo:
        if clave.lower() in producto["Título"].lower():
            productos_encontrados.append(producto)

    if productos_encontrados:
        print("\nProducto(s) encontrado(s):\n")
        for producto in productos_encontrados:
            print(f"- {producto['Título']} ({producto['Tipo']})")
    else:
        print("\nNo se encontraron productos que coincidan con la búsqueda")

    continuar()
    return

def mostrar_catalogo(catalogo):
    """
    Muestra el catálogo completo o por categoría.
    Solicita al usuario seleccionar la opción de visualización y muestra los productos correspondientes.
    """
    if catalogo is None:
        print('No existe un catálogo para mostrar.')
        continuar()
        return

    while True:
        print("¿Qué desea mostrar?:\n")
        print("1. Películas")
        print("2. Series")
        print("3. Documentales")
        print("4. Eventos deportivos")
        print("5. Todo")
        print("6. Regresar")

        opciones = {'1': 'Película', '2': 'Serie', '3': 'Documental', '4': 'Evento deportivo en vivo'}
        opcion = input("\nSeleccione una opción: ")

        if opcion in opciones.keys():
            espera()
            tipo = opciones[opcion]
            productos = [producto for producto in catalogo if producto['Tipo'].lower() == tipo.lower()]
            if productos:
                print(f'\nMostrando {tipo}:\n')
                for producto in productos:
                    for cat, dat in producto.items():
                        print(f'- {cat}: {dat}')
                    print()
            else:
                print(f'\nNo existen productos en {tipo}.')
            continuar()
        elif opcion == '5':
            espera()
            for tipo in opciones.values():
                productos = [producto for producto in catalogo if producto['Tipo'].lower() == tipo.lower()]
                if productos:
                    print(f'\nMostrando {tipo}:\n')
                    for producto in productos:
                        for cat, dat in producto.items():
                            print(f'- {cat}: {dat}')
                        print()                    
                else:
                    print(f'\nNo existen productos en {tipo}.')
                print()
                print('-'*25)
            continuar()
        elif opcion == '6':
            print('\nRegresando al menú principal. . .')
            espera()
            return
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            continuar()

def eliminar_producto(catalogo):
    """
    Permite eliminar un producto del catálogo.
    Solicita al usuario el título del producto a eliminar y lo elimina del catálogo si existe.
    """
    if catalogo is None:
        print('No existe un catálogo.')
        continuar()
        return

    titulo = input("Ingrese el título del producto que desea eliminar: ")
    producto_encontrado = False

    for producto in catalogo:
        if titulo.lower() == producto["Título"].lower():
            producto_encontrado = producto
            break

    if producto_encontrado:
        catalogo.remove(producto_encontrado)
        print("\nProducto eliminado
