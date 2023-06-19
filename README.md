[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
# Proyecto
Equipo:
Candelaria Rivera Emiliano.
Torres Aguilar Alan.

Diagrama de estructura

![](https://github.com/agn-pe-23i/proyecto-los-mas-pythones/blob/main/Diagrama%20Estructural.png)

Documentación del uso de modulos y del programa principal

El programa es un sistema de gestión de catálogos de productos de sreaming. 

Clases:

Pelicula: Representa una película y tiene los siguientes atributos:

titulo: Título de la película.
actor_principal: Actor principal de la película.
director: Director de la película.
anio: Año de lanzamiento de la película.
costo_renta: Costo de renta de la película.
costo_venta: Costo de venta de la película.

Serie: Representa una serie y tiene los siguientes atributos:

titulo: Título de la serie.
actor_principal: Actor principal de la serie.
director: Director de la serie.
temporadas: Número de temporadas de la serie.
costo_renta: Costo de renta de la serie.
costo_venta: Costo de venta de la serie.

Documental: Representa un documental y tiene los siguientes atributos:

titulo: Título del documental.
director: Director del documental.
tema: Tema del documental.
anio: Año de lanzamiento del documental.
costo_renta: Costo de renta del documental.
costo_venta: Costo de venta del documental.

EventoDeportivo: Representa un evento deportivo y tiene los siguientes atributos:

titulo: Título del evento deportivo.
deporte: Deporte del evento.
fecha: Fecha del evento.
hora: Hora del evento.
lugar: Lugar del evento.
costo_venta: Costo de venta del evento deportivo.

Funciones:

menu_principal(): Muestra el menú principal del programa y permite al usuario seleccionar diferentes opciones como agregar producto, buscar producto, eliminar producto, mostrar catálogo, cargar catálogo desde archivo, guardar catálogo en archivo y salir.

guardar_catalogo(): Guarda el catálogo actual en un archivo. El usuario debe ingresar el nombre del archivo.

agregar_producto(): Permite al usuario agregar un producto al catálogo. El usuario puede seleccionar el tipo de producto (película, serie, documental o evento deportivo) y luego ingresar la información correspondiente.

buscar_producto(): Permite al usuario buscar productos en el catálogo utilizando palabras clave. Muestra los productos que coinciden con la búsqueda.

eliminar_producto(): Permite al usuario eliminar un producto del catálogo. El usuario debe ingresar el título del producto a eliminar.

mostrar_catalogo(): Muestra el catálogo de productos al usuario. El usuario puede seleccionar diferentes opciones para mostrar solo películas, series, documentales, eventos deportivos o todo el catálogo.

cargar_catalogo(): Carga el catálogo de productos desde un archivo. El usuario debe ingresar el nombre del archivo.


Implementación y diseño del programa


Clases de productos

El programa inicia definiendo 4 clases de productos: ‘Película’, ‘Serie’, ‘Documental’ y ‘EventoDeportivos’. Cada clase tiene un constructor ‘_init_’, para poder inicializar los atributos específicos de cada producto. Por ejemplo, la clase 'Pelicula' tiene atributos como titulo, actor_principal, director, anio, costo_renta y costo_venta. Estas clases representan la estructura de datos para cada tipo de producto en el catálogo.

![](https://github.com/agn-pe-23i/proyecto-los-mas-pythones/blob/main/Imagen1.png)
imagen 1

Por ejemplo, en la imagen 1 vemos el caso de la clase ‘Película’, donde sus atributos caracteristicos son “titulo”, “actor_principal”, “director” y “año”, además de incluir el “costo_renta” y costo_venta”. Las clases representaran la estructura de datos para cada tipo de producto en el catalogo. 

Menú principal

Posteriormente a la implementación de las clases encontramos el módulo del menú principal ‘menu_principal()’, el cual es el punto de entrada del programa y muestra el menú de opciones al usuario. 

![](https://github.com/agn-pe-23i/proyecto-los-mas-pythones/blob/main/Imagen2.png)
imagen 2
![](https://github.com/agn-pe-23i/proyecto-los-mas-pythones/blob/main/Imagen3.png)
imagen 3

Tanto en las imagenes 2 y 3 observamos la implementación de un bucle en el que la única forma de detener la ejecución del programa es con la opción 6 de ‘Salir’. Las opciones se implementaron dentro de una estructura de control de selección múltiple de forma que el usuario pueda escoger solo una de las opciones. Si se escoge una opción que no esté dentro de la función entonces se desplegara un mensaje avisando de que no es una opción viable y que debe escoger una opción válida.

Agregar productos

El funcionamiento del modulo ‘agregar_producto()’ es permitir al usuario agregar un nuevo producto al catálogo. Se tendrán 5 opciones, 4 para determinar que tipo de producto se desea agregar y una quinta por si se prefiere regresar al menú principal. Dependiendo de la opción seleccionada se solicitara la información especifica del tipo de producto correspondiente. 

![](https://github.com/agn-pe-23i/proyecto-los-mas-pythones/blob/main/Imagen4.png)
imagen 4

Ejemplificando lo anterior, en la ilustración 4 se muestra que si el usuario escogió la opción 2 dentro de la función de ‘agregar_producto()’ entonces se agregara un producto de tipo serie por lo que se preguntara por sus atributos para posteriormente guardarlos dentro del catálogo. 

Buscar producto

Este módulo permite al usuario hacer búsquedas de un producto a partir de la solicitud de palabras claves del programa hacia el usuario. 

![](https://github.com/agn-pe-23i/proyecto-los-mas-pythones/blob/main/Imagen5.png)
imagen 5

Al inicio de la función implementamos una estructura ‘for’ que compare las palabras claves solicitadas con los productos contenidos en el catalogo y si estos coinciden con el título de algún producto el producto se guardara dentro de una lista. Si finalmente resulta que hay una coincidencia utilizando una estructura de control seletivo anidamos una estrucutrura 'for' para que el producto se despliegue junto con toda su información correspondiente. 

Eliminar producto

La función 'eliminar_producto()' permite al usuario eliminar un producto del catálogo. Se solicita el título del producto a eliminar y se busca en el catálogo. Si se encuentra, se elimina del catálogo. Para esto se implemento una estructura de control selectivo anidada en una estrucutrua 'for' para que si el producto se encuentre dentro del catalogo entonces este sea eliminado. 

Mostrar Catálogo

La función 'mostrar_catalogo()' muestra al usuario diferentes opciones para mostrar el catálogo. Dependiendo de la opción seleccionada (1, 2, 3, 4, 5 o 6), se muestra una lista de productos filtrada por tipo o se muestra todo el catálogo completo.
Se utiliza una estrucutra de control selectivo múltiple para que el usuario pueda escoger una opción de producto que desee que el programa le muestre del catálogo o bien también hay una opción para para que se muestre todo el catálogo.

![](https://github.com/agn-pe-23i/proyecto-los-mas-pythones/blob/main/Imagen6.png)
imagen 6

Podemos observar de la imagen 6 que anidado a la estructura antes mencionada hay un 'for' que se utiliza para que todos los productos que sean del mismo tipo se muestren, en el ejemplo podemos ver el producto de clase 'Pelicula', el modulo desplegará la información de cada producto. 

Cargar catálogo

Primero se solicita que se ingrese el nombre del archivo de catálogo utilizando la función 'input()'. Continuando se implementa un bloque 'try-except' para manejar los posibles errores al abrir y leer un archivo. Dentro del bloque 'try', abre el archivo usando la función 'open()' en modo lectura "r" y lo asocia a suna variable llamada 'archivo'. Se leen todas las líneas del archivo utilizando el metodo 'readlines()', que devuelve una lista de cadenas, donde cada cadena representa una línea del archivo.

![](https://github.com/agn-pe-23i/proyecto-los-mas-pythones/blob/main/Imagen7.png)
imagen 7

En la imagen 7 podemos ver la implementación de un bucle 'for linea in lineas:', que recorre cada una de las lineas del archivo. Para cada linea se realiza lo siguiente: Se eliminan los espacios en blanco iniciales y finales de la línea utilizando 'strip()'. Y se divide la línea en diferentes parates utilizando 'split(",")', lo que crea una lista donde cada elemento es una parte separa por comas. Con una estructura de control selectiva multiple se verifica que el primer elemento de la lista 'datos' para determianr el tipo de elemento en el catálogo. Dependiendo del valor, los datos de se agrega a la lista de catalogo con la funcion '.append()'.

Guardar catálogo

Se solicita al usuario que ingrese el nombre del archivo en el cual desea guardar el catálogo utilizando la función 'input()'. Utilizamos un bloque 'try-except' para manejar posibles errores al abrir y escribir en el archivo. Dentro del bloque 'try', abre el archivo utilizando la función 'open()' en modo de escritura "w" y lo asocia a una variable llamada archivo. Se recorre cada producto en el catálogo utilizando el bucle 'for producto in catalogo:'. Para cada producto, se verifica su tipo utilizando la función 'isinstance()' y se ejecuta el código correspondiente al tipo de producto.

![](https://github.com/agn-pe-23i/proyecto-los-mas-pythones/blob/main/Imagen8.png)
imagen 8

Como se observa en la imagen 8, dependiendo de la instancia de la clase a la que pertenece el producto se creara una inea de texto que contiene los valores del producto separados por comas y agrega un salto de línea al final. Terminando el bucle se encuentra la funcion '.write()' que almacenara cada línea de producto dentro del archivo txt que se haya indicado.
