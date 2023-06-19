[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
# Proyecto
Equipo:
Candelaria Rivera Emiliano.
Torres Aguilar Alan.

Diagrama de estructura

![](https://github.com/agn-pe-23i/proyecto-los-mas-pythones/blob/main/Diagrama%20Estructural.png)

Documentación del uso de modulos y del programa principal



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

![]()
imagen 7


Guardar catálogo
