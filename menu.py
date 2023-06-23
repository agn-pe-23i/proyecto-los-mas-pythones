import time
import os

# Funcion para realizar una pausa de 1 segundo. 
def espera():
    time.sleep(1)  # suspende la ejecución del programa durante el número de segundos especificados
    os.system('cls' if os.name == 'nt' else 'clear')  # comando para limpiar la pantalla.

# Función que espera la pulsación de la tecla enter para continuar la ejecución del programa.
def continuar():a
    input('\nPresione Enter para continuar. . .')  # Se espera que el usuario presione la tecla enter para continuar la ejecución del programa.
    os.system('cls' if os.name == 'nt' else 'clear')  # comando para limpiar la pantalla.

# Función para acceder a una al diccionario de datos. 
def datosProducto(opcion):
    datos = {
        'Película': ['Título', 'Actor principal', 'Director', 'Año', 'Precio de renta', 'Precio de venta'],
        'Serie': ['Título', 'Actor principal', 'Director', 'Temporadas', 'Precio de renta', 'Precio de venta'],
        'Documental': ['Título', 'Actor principal', 'Director', 'Tema', 'Año', 'Precio de renta', 'Precio de venta'],
        'Evento deportivo en vivo': ['Título', 'Deporte', 'Fecha', 'Hora', 'Lugar', 'Precio de venta']
    }

    return datos[opcion]

# Función para agregar un producto al catálogo
def agregar_producto(catalogo):
    """
    Esta función permite agregar un producto al catálogo.
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

        # El diccionario opciones nos ayuda a verificar si la opción que se ingresa sea válida 
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
        print("\nProducto eliminado correctamente.")
    else:
        print("\nNo se encontró un producto con el título especificado.")
    
    continuar()
    return
