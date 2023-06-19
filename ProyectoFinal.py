
# Definición de la estructura de datos para cada tipo de producto
class Pelicula:
    def __init__(self, titulo, actor_principal, director, anio, costo_renta, costo_venta):
        self.titulo = titulo
        self.actor_principal = actor_principal
        self.director = director
        self.anio = anio
        self.costo_renta = costo_renta
        self.costo_venta = costo_venta

class Serie:
    def __init__(self, titulo, actor_principal, director, temporadas, costo_renta, costo_venta):
        self.titulo = titulo
        self.actor_principal = actor_principal
        self.director = director
        self.temporadas = temporadas
        self.costo_renta = costo_renta
        self.costo_venta = costo_venta

class Documental:
    def __init__(self, titulo, director, tema, anio, costo_renta, costo_venta):
        self.titulo = titulo
        self.director = director
        self.tema = tema
        self.anio = anio
        self.costo_renta = costo_renta
        self.costo_venta = costo_venta

class EventoDeportivo:
    def __init__(self, titulo, deporte, fecha, hora, lugar, costo_venta):
        self.titulo = titulo
        self.deporte = deporte
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar
        self.costo_venta = costo_venta

# Catálogo de productos
catalogo = []
def menu_principal():
    while True:
        print("Menú principal:")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Eliminar producto")
        print("4. Mostrar catálogo")
        print("5. Cargar catálogo desde archivo")
        print("6. Guardar catálogo en archivo")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            mostrar_catalogo()
        elif opcion == "5":
            cargar_catalogo()
        elif opcion == "6":
            guardar_catalogo()
        elif opcion == "7":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def guardar_catalogo():
    nombre_archivo = input("Ingrese el nombre del archivo para guardar el catálogo: ")
    try:
        with open(nombre_archivo, "w") as archivo:
            for producto in catalogo:
                if isinstance(producto, Pelicula):
                    tipo_producto = "Pelicula"
                    linea = f"{tipo_producto},{producto.titulo},{producto.actor_principal},{producto.director},{producto.anio},{producto.costo_venta},{producto.costo_renta}\n"
                elif isinstance(producto, Serie):
                    tipo_producto = "Serie"
                    linea = f"{tipo_producto},{producto.titulo},{producto.director},{producto.actor_principal}{producto.temporadas},{producto.costo_venta}{producto.costo_renta},\n"
                elif isinstance(producto, Documental):
                    tipo_producto = "Documental"
                    linea = f"{tipo_producto},{producto.titulo},{producto.director},{producto.anio},{producto.tema},{producto.costo_renta},{producto.costo_venta}\n"
                elif isinstance(producto, EventoDeportivo):
                    tipo_producto = "Evento deportivo en vivo"
                    linea = f"{tipo_producto},{producto.titulo},{producto.deporte},{producto.fecha},{producto.hora},{producto.lugar},{producto.costo_venta}\n"

                else:
                    continue
                archivo.write(linea)
            print("Catálogo guardado exitosamente.")

    except IOError:
        print("Error al guardar el catálogo en el archivo.")


# Función para agregar un producto al catálogo
def agregar_producto():
    """
    Esta función permite agregar un producto al catálogo.
    Solicita al usuario la información correspondiente y crea una instancia
    del tipo de producto seleccionado para luego agregarlo al catálogo.
    """
    print("Menú agregar producto:")
    print("1. Película")
    print("2. Serie")
    print("3. Documental")
    print("4. Evento deportivo en vivo")
    print("5. Regresar")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Solicitar información de la película
        titulo = input("Ingrese el título: ")
        actor_principal = input("Ingrese el actor principal: ")
        director = input("Ingrese el director: ")
        anio = input("Ingrese el año: ")
        costo_renta = float(input("Ingrese el costo de renta: "))
        costo_venta = float(input("Ingrese el costo de venta: "))

        # Crear una instancia de Pelicula y agregarla al catálogo
        pelicula = Pelicula(titulo, actor_principal, director, anio, costo_renta, costo_venta)
        catalogo.append(pelicula)

        print("Pelicula agregada exitosamente.")
    elif opcion == "2":
        # Solicitar información de la serie
        titulo = input("Ingrese el título: ")
        actor_principal = input("Ingrese el actor principal: ")
        director = input("Ingrese el director: ")
        temporadas = int(input("Ingrese el número de temporadas: "))
        costo_renta = float(input("Ingrese el costo de renta: "))
        costo_venta = float(input("Ingrese el costo de venta: "))

        # Crear una instancia de Serie y agregarla al catálogo
        serie = Serie(titulo, actor_principal, director, temporadas, costo_renta, costo_venta)
        catalogo.append(serie)

        print("Serie agregada exitosamente.")
    elif opcion == "3":
        # Solicitar información del documental
        titulo = input("Ingrese el título: ")
        director = input("Ingrese el director: ")
        tema = input("Ingrese el tema: ")
        anio = input("Ingrese el año: ")
        costo_renta = float(input("Ingrese el costo de renta: "))
        costo_venta = float(input("Ingrese el costo de venta: "))

        # Crear una instancia de Documental y agregarla al catálogo
        documental = Documental(titulo, director, tema, anio, costo_renta, costo_venta)
        catalogo.append(documental)

        print("Documental agregado exitosamente.")
    elif opcion == "4":
        # Solicitar información del evento deportivo
        titulo = input("Ingrese el título: ")
        deporte = input("Ingrese el deporte: ")
        fecha = input("Ingrese la fecha: ")
        hora = input("Ingrese la hora: ")
        lugar = input("Ingrese el lugar: ")
        costo_venta = float(input("Ingrese el costo de venta: "))

        # Crear una instancia de EventoDeportivo y agregarla al catálogo
        evento = EventoDeportivo(titulo, deporte, fecha, hora, lugar, costo_venta)
        catalogo.append(evento)

        print("Evento deportivo agregado exitosamente.")
    elif opcion == "5":
        # Regresar al menú principal
        return
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

    # Luego de agregar un producto, se puede llamar a la función recursivamente para agregar más productos
    agregar_producto()
def buscar_producto():
    palabras_clave = input("Ingrese las palabras clave para la búsqueda: ")
    resultados = []
    for producto in catalogo:
        if palabras_clave.lower() in producto.titulo.lower():
            resultados.append(producto)

    if len(resultados) > 0:
        print("Resultados de la búsqueda:")
        for producto in resultados:
            if isinstance(producto, Pelicula):
                tipo_producto = "Película"
                print("Tipo: " + tipo_producto)
                print("Título:", producto.titulo)
                print("Actor Principal:", producto.actor_principal)
                print("Director:", producto.director)
                print("Año:", producto.anio)
                print("Precio de Renta:", producto.costo_renta)
                print("Precio de Venta:", producto.costo_venta)
                print("---------------------")
            elif isinstance(producto, Serie):
                tipo_producto = "Serie"
                print("Tipo: " + tipo_producto)
                print("Título:", producto.titulo)
                print("Actor Principal:", producto.actor_principal)
                print("Director:", producto.director)
                print("Temporadas:", producto.temporadas)
                print("Precio de Renta:", producto.costo_renta)
                print("Precio de Venta:", producto.costo_venta)
                print("---------------------")
            elif isinstance(producto, Documental):
                tipo_producto = "Documental"
                print("Tipo: " + tipo_producto)
                print("Título:", producto.titulo)
                print("Director:", producto.director)
                print("Tema:", producto.tema)
                print("Año:", producto.anio)
                print("Precio de Renta:", producto.costo_renta)
                print("Precio de Venta:", producto.costo_venta)
                print("---------------------")
            elif isinstance(producto, EventoDeportivo):
                tipo_producto = "Evento deportivo en vivo"
                print("Tipo: " + tipo_producto)
                print("Título:", producto.titulo)
                print("Deporte:", producto.deporte)
                print("Fecha:", producto.fecha)
                print("Hora:", producto.hora)
                print("Lugar:", producto.lugar)
                print("Precio de Venta:", producto.costo_venta)
                print("---------------------")
    else:
        print("No se encontraron productos que coincidan con la búsqueda.")

def eliminar_producto():
    titulo = input("Ingrese el título del producto a eliminar: ")
    encontrado = False
    for producto in catalogo:
        if producto.titulo.lower() == titulo.lower():
            catalogo.remove(producto)
            encontrado = True
            break

    if encontrado:
        print("Producto eliminado exitosamente.")
    else:
        print("No se encontró el producto en el catálogo.")

def mostrar_catalogo():
    print("Menú mostrar catálogo:")
    print("1. Películas")
    print("2. Series")
    print("3. Documentales")
    print("4. Eventos deportivos")
    print("5. Todo")
    print("6. Regresar")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Mostrar solo películas
        print("Películas:")
        for producto in catalogo:
            if isinstance(producto, Pelicula):
                print("Título:", producto.titulo)
                print("Actor Principal:", producto.actor_principal)
                print("Director:", producto.director)
                print("Año:", producto.anio)
                print("Precio de Renta:", producto.costo_renta)
                print("Precio de Venta:", producto.costo_venta)
                print("---------------------")
    elif opcion == "2":
        # Mostrar solo series
        print("Series:")
        for producto in catalogo:
            if isinstance(producto, Serie):
                print("Título:", producto.titulo)
                print("Actor Principal:", producto.actor_principal)
                print("Director:", producto.director)
                print("Temporadas:", producto.temporadas)
                print("Precio de Renta:", producto.costo_renta)
                print("Precio de Venta:", producto.costo_venta)
                print("---------------------")
    elif opcion == "3":
        # Mostrar solo documentales
        print("Documentales:")
        for producto in catalogo:
            if isinstance(producto, Documental):
                print("Título:", producto.titulo)
                print("Director:", producto.director)
                print("Tema:", producto.tema)
                print("Año:", producto.anio)
                print("Precio de Renta:", producto.costo_renta)
                print("Precio de Venta:", producto.costo_venta)
                print("---------------------")
    elif opcion == "4":
        # Mostrar solo eventos deportivos
        print("Eventos deportivos:")
        for producto in catalogo:
            if isinstance(producto, EventoDeportivo):
                print("Título:", producto.titulo)
                print("Deporte:", producto.deporte)
                print("Fecha:", producto.fecha)
                print("Hora:", producto.hora)
                print("Lugar:", producto.lugar)
                print("Precio de Venta:", producto.costo_venta)
                print("---------------------")
    elif opcion == "5":
        # Mostrar todo el catálogo
        print("Catálogo completo:")
        for producto in catalogo:
            if isinstance(producto, Pelicula):
                tipo_producto = "Película"
            elif isinstance(producto, Serie):
                tipo_producto = "Serie"
            elif isinstance(producto, Documental):
                tipo_producto = "Documental"
            elif isinstance(producto, EventoDeportivo):
                tipo_producto = "Evento deportivo en vivo"

            print("Tipo:", tipo_producto)
            print("Título:", producto.titulo)
            print("---------------------")
    elif opcion == "6":
        return
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        #en esta parte se cargan los datos del archivo .txt
def cargar_catalogo():
    nombre_archivo = input("Ingrese el nombre del archivo de catálogo: ")
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")  # Separar los datos por coma

                if datos[0] == "Pelicula":
                    titulo = datos[1]
                    actor_principal = datos[2]
                    director = datos[3]
                    anio = datos[4]
                    costo_renta = float(datos[5])
                    costo_venta = float(datos[6])

                    pelicula = Pelicula(titulo, actor_principal, director, anio, costo_renta, costo_venta)
                    catalogo.append(pelicula)
                elif datos[0] == "Serie":
                    titulo = datos[1]
                    actor_principal = datos[2]
                    director = datos[3]
                    temporadas = int(datos[4])
                    costo_renta = float(datos[5])
                    costo_venta = float(datos[6])

                    serie = Serie(titulo, actor_principal, director, temporadas, costo_renta, costo_venta)
                    catalogo.append(serie)
                elif datos[0] == "Documental":
                    titulo = datos[1]
                    director = datos[2]
                    tema = datos[3]
                    anio = datos[4]
                    costo_renta = float(datos[5])
                    costo_venta = float(datos[6])

                    documental = Documental(titulo, director, tema, anio, costo_renta, costo_venta)
                    catalogo.append(documental)
                elif datos[0] == "EventoDeportivo":
                    titulo = datos[1]
                    deporte = datos[2]
                    fecha = datos[3]
                    hora = datos[4]
                    lugar = datos[5]
                    costo_venta = float(datos[6])

                    evento = EventoDeportivo(titulo, deporte, fecha, hora, lugar, costo_venta)
                    catalogo.append(evento)

        print("Catálogo cargado exitosamente.")
    except FileNotFoundError:
        print("El archivo no existe.")
    except PermissionError:
        print("No se puede acceder al archivo.")
menu_principal()