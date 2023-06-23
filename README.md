[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
# Proyecto
Equipo:
Candelaria Rivera Emiliano.
Torres Aguilar Alan.

Diagrama de estructura

![](https://github.com/agn-pe-23i/proyecto-los-mas-pythones/blob/main/Diagrama%20Estructural.png)

- El diagrama de estrucutura esta hecho para visualizar como se realizaron los modulos para satisfacer el cumplimeinto del programa.
- Se creo la función principal 'main' en la cual controla los demás modulos. Los modulos principales para cargar y guardar un archivo reciben un 'catalogo' el cual es una lista de diccionarios donde se encuentran los productos de nuestro catalogo.
- Las funciones que manipulan el catalogo son 'agregar_producto', 'buscar_producto', 'eliminar_producto' y 'mostrar_catalogo'.

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

Este programa se implemento con una estrucutra modular. Se crearon tres scripts para mostrar y ejecutar de forma clara cada uno de los modulos. 

 Implementación del script 'main.py'

Describe la implementación del script 'main' en Python para un programa modular. El script principal es responsable de controlar las interacciones con el catálogo de productos, permitiendo agregar, buscar, eliminar, mostrar y gestionar el catálogo mediante opciones del script de archivos.py donde estan los modulos de cargar y guardar el catálogo. 

Objetivos

Permitir al usuario interactuar con el catálogo de productos de forma intuitiva y eficiente.
Proporcionar funciones para agregar, buscar, eliminar, mostrar y gestionar el catálogo.
Cargar y guardar el catálogo desde y hacia un archivo.

Herramientas utilizadas

Módulos estándar: sys, os, time
Módulos personalizados: menu, archivos

Estructura del script principal

El script principal comienza con las importaciones de los módulos y bibliotecas necesarias, seguidas por la definición de una variable global catalogo que almacena el catálogo de productos.

Funciones y variables principales

La función main() es el punto de entrada principal del programa. Controla el flujo del menú y las opciones seleccionadas por el usuario.
La variable global catalogo almacena el catálogo de productos y se actualiza a medida que se realizan cambios en el catálogo.

Menú principal

El menú principal muestra opciones numeradas para realizar diferentes acciones en el catálogo de productos.
El usuario selecciona una opción ingresando el número correspondiente.
Según la opción seleccionada, se llaman a funciones del módulo menu para realizar las tareas específicas, como agregar un producto, buscar un producto, eliminar un producto, mostrar el catálogo, cargar el catálogo desde un archivo o guardar el catálogo en un archivo.
El menú se repite hasta que el usuario seleccione la opción de salir.

Interacción con otros módulos

El script principal interactúa con dos módulos adicionales: menu y archivos.
El módulo menu proporciona las funciones necesarias para realizar las acciones del menú, como agregar, buscar, eliminar y mostrar productos, así como funciones de espera y continuidad.
El módulo archivos ofrece funciones para cargar y guardar el catálogo desde y hacia un archivo.

Implementación

El script principal se implementa siguiendo un enfoque modular.
Se utiliza un bucle while para mostrar el menú principal y manejar las opciones seleccionadas por el usuario.
Las funciones del módulo menu se llaman según la opción seleccionada por el usuario.
El catálogo se actualiza según las modificaciones realizadas por el usuario.
Resultados y análisis

Al ejecutar el script principal, se muestra el menú principal y se espera la selección del usuario.
Dependiendo de la opción elegida, se realizan diferentes acciones en el catálogo de productos, como agregar, buscar, eliminar o mostrar productos.
El catálogo se puede cargar desde un archivo existente o guardarse en un archivo para su uso.

Implementación del módulo de 'menú' en Python

Se describe la implementación del módulo 'menu' para un programa modular. El módulo menu contiene funciones relacionadas con la interacción del usuario, como mostrar el menú, agregar productos, buscar productos, mostrar el catálogo y eliminar productos.

Objetivos

Proporcionar un menú intuitivo y fácil de usar para que el usuario interactúe con el catálogo de productos.
Permitir al usuario agregar, buscar, mostrar y eliminar productos de manera eficiente.
Proporcionar funciones de espera y continuidad para mejorar la experiencia del usuario.

Herramientas utilizadas

Módulos estándar: time, os

Funciones principales

La función espera() agrega un tiempo de espera de 1 segundo para mejorar la legibilidad del programa y luego borra la pantalla de la consola.
La función continuar() espera a que el usuario presione Enter antes de continuar y luego borra la pantalla de la consola.
La función datosProducto(opcion) devuelve una lista de datos específicos según la opción seleccionada, utilizada para agregar productos al catálogo.
La función agregar_producto(catalogo) permite al usuario agregar un producto al catálogo. Solicita la información necesaria y crea una instancia del tipo de producto seleccionado.
La función buscar_producto(catalogo) permite al usuario buscar productos en el catálogo utilizando palabras clave. Muestra los productos encontrados que coinciden con la búsqueda.
La función mostrar_catalogo(catalogo) permite al usuario mostrar el catálogo completo o filtrado por tipo de producto. Muestra los productos del catálogo en la consola.
La función eliminar_producto(catalogo) permite al usuario eliminar un producto del catálogo según su título. Verifica si el producto existe en el catálogo y lo elimina si se encuentra.

Implementación

El módulo menu se implementa como un conjunto de funciones que se importan y utilizan en el script principal.
Cada función realiza una tarea específica relacionada con la interacción del usuario en el menú.
Las funciones utilizan las funciones espera() y continuar() para mejorar la legibilidad y la experiencia del usuario.
Resultados y análisis

Al utilizar las funciones del módulo menu, el usuario puede interactuar con el catálogo de productos de manera eficiente.
El menú muestra opciones claras y permite al usuario agregar, buscar, mostrar y eliminar productos según sus necesidades.
Las funciones de espera y continuidad mejoran la experiencia del usuario al proporcionar pausas y limpiar la pantalla de la consola

Implementación del script para manejo de archivos en Python

SE describe la implementación del script archivos.py en Python, que contiene funciones relacionadas con el manejo de archivos para cargar y guardar el catálogo de productos en formato JSON.

Objetivos

Proporcionar funciones para cargar y guardar el catálogo de productos en archivos JSON.
Manejar casos de error al cargar o guardar el catálogo.
Interactuar con el usuario para obtener el nombre del archivo y brindar información sobre el estado de la operación.

Herramientas utilizadas

Módulos estándar: json
Módulo personalizado: menu

Funciones principales

La función cargar_catalogo() permite al usuario cargar el catálogo de productos desde un archivo JSON. Solicita el nombre del archivo al usuario, lo carga y devuelve el catálogo como un diccionario.
La función guardar_catalogo(catalogo) permite al usuario guardar el catálogo de productos en un archivo JSON. Solicita el nombre del archivo y guarda el catálogo en formato JSON.

Implementación

El script archivos.py importa el módulo json para trabajar con archivos JSON y el módulo personalizado menu para mostrar mensajes al usuario.
La función cargar_catalogo() solicita el nombre del archivo al usuario y lo abre en modo lectura. Si el archivo existe y está en formato JSON válido, carga el catálogo y muestra un mensaje de éxito. Si hay un error en el proceso, muestra un mensaje correspondiente y devuelve None.
La función guardar_catalogo(catalogo) solicita el nombre del archivo al usuario y lo abre en modo escritura. Si el catálogo no es None, se guarda en formato JSON en el archivo especificado y se muestra un mensaje de éxito. Si hay un error en el proceso, muestra un mensaje correspondiente.
Resultados y análisis

Utilizando las funciones cargar_catalogo() y guardar_catalogo(catalogo), se puede interactuar con archivos JSON para cargar y guardar el catálogo de productos.
