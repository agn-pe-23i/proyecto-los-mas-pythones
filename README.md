[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
# Proyecto
Equipo:
Candelaria Rivera Emiliano.
Torres Aguilar Alan.

Diagrama de estructura

![]()

Documentación del uso de modulos y del programa principal

Documentación del Código

El código proporcionado contiene varias funciones que permiten la gestión de un catálogo de productos. A continuación, se describe cada una de las funciones y su funcionalidad.

Funciones Principales

1. **`cargar_catalogo()`**: Esta función se encarga de cargar un catálogo desde un archivo JSON. Solicita al usuario el nombre del archivo de catálogo a cargar (sin la extensión .json). Luego, intenta abrir el archivo y cargar su contenido en formato JSON. Si el archivo no existe, muestra un mensaje de error. Si el archivo no está en un formato válido, también muestra un mensaje de error. Retorna el catálogo cargado o `None` si hubo algún error.

2. **`guardar_catalogo(catalogo)`**: Esta función guarda un catálogo en un archivo JSON. Recibe como parámetro el catálogo a guardar. Si el catálogo es `None`, muestra un mensaje de error. Luego, solicita al usuario el nombre del archivo donde se guardará el catálogo. Intenta guardar el catálogo en formato JSON en el archivo especificado. Si no se puede guardar el catálogo, muestra un mensaje de error.

 Funciones para la Manipulación del Catálogo

3. **`agregar_producto(catalogo)`**: Esta función permite agregar un producto al catálogo. Solicita al usuario seleccionar el tipo de producto a agregar (película, serie, documental o evento deportivo en vivo) y luego solicita los datos correspondientes. Crea un diccionario con los datos ingresados y lo agrega al catálogo. Si el catálogo es `None`, lo inicializa como una lista vacía. Muestra mensajes de éxito o error según corresponda.

4. **`buscar_producto(catalogo)`**: Esta función permite buscar productos en el catálogo utilizando palabras clave del título. Solicita al usuario ingresar las palabras clave y busca los productos cuyo título contenga dichas palabras clave (ignorando mayúsculas y minúsculas). Muestra los productos encontrados o un mensaje indicando que no se encontraron productos.

5. **`mostrar_catalogo(catalogo)`**: Esta función permite mostrar el catálogo completo o filtrado por tipo de producto. Solicita al usuario seleccionar qué desea mostrar y muestra los productos correspondientes. Puede mostrar películas, series, documentales, eventos deportivos o todo el catálogo. Si no hay productos en alguna categoría, muestra un mensaje indicando que no existen productos en esa categoría.

6. **`eliminar_producto(catalogo)`**: Esta función permite eliminar un producto del catálogo. Solicita al usuario ingresar el título del producto a eliminar y busca en el catálogo un producto con ese título (ignorando mayúsculas y minúsculas). Si encuentra el producto, lo elimina del catálogo. Muestra mensajes de éxito o error según corresponda.

Funciones de Utilidad

7. **`continuar()`**: Esta función solicita al usuario presionar Enter para continuar. Se utiliza para pausar el programa y dar tiempo al usuario para leer los mensajes.

8. **`espera()`**: Esta función realiza una pausa de 1 segundo y luego limpia la pantalla. Utiliza la función `time.sleep()` para generar la pausa y la función `os.system()` para limpiar la pantalla, utilizando comandos específicos dependiendo del sistema operativo.

9. **`datosProducto(opcion)`**: Esta función devuelve los datos requeridos para un tipo de producto específico. Recibe como parámetro la opción seleccionada por el usuario y devuelve una lista con los datos requeridos para el tipo de producto seleccionado.



Implementación y diseño del programa



