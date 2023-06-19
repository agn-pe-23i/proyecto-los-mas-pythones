[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
# Proyecto
Diagrama de estructura

![]()

Implementación y diseño del programa


Clases de productos

El programa inicia definiendo 4 clases de productos: ‘Película’, ‘Serie’, ‘Documental’ y ‘EventoDeportivos’. Cada clase tiene un constructor ‘_init_’, para poder inicializar los atributos específicos de cada producto. Por ejemplo, la clase 'Pelicula' tiene atributos como titulo, actor_principal, director, anio, costo_renta y costo_venta. Estas clases representan la estructura de datos para cada tipo de producto en el catálogo.

![](https://github.com/agn-pe-23i/proyecto-los-mas-pythones/blob/main/Imagen1.png)
imagen 1

Por ejemplo, en la imagen 1 vemos el caso de la clase ‘Película’, donde sus atributos caracteristicos son “titulo”, “actor_principal”, “director” y “año”, además de incluir el “costo_renta” y costo_venta”. Las clases representaran la estructura de datos para cada tipo de producto en el catalogo. 

Menú principal

Posteriormente a la implementación de las clases encontramos el módulo del menú principal ‘menu_principal()’, el cual es el punto de entrada del programa y muestra el menú de opciones al usuario. 

![](https://github.com/agn-pe-23i/proyecto-los-mas-pythones/blob/main/Imagen2.png)

![]()

Tanto en las imagenes 2 y 3 observamos la implementación de un bucle en el que la única forma de detener la ejecución del programa es con la opción 6 de ‘Salir’. Las opciones se implementaron dentro de una estructura de control de selección múltiple de forma que el usuario pueda escoger solo una de las opciones. Si se escoge una opción que no esté dentro de la función entonces se desplegara un mensaje avisando de que no es una opción viable y que debe escoger una opción válida.

Agregar productos

El funcionamiento del modulo ‘agregar_producto()’ es permitir al usuario agregar un nuevo producto al catálogo. Se tendrán 5 opciones, 4 para determinar que tipo de producto se desea agregar y una quinta por si se prefiere regresar al menú principal. Dependiendo de la opción seleccionada se solicitara la información especifica del tipo de producto correspondiente. 

Buscar producto

Este módulo permite al usuario hacer búsquedas de un producto a partir de la solicitud de palabras claves del programa hacia el usuario. 

Al inicio de la función implementamos una estructura ‘for’ que compare las palabras claves solicitadas con los productos contenidos en el catalogo y si estos coinciden con el título de algún producto el producto se guardara dentro de una lista. 

Si la busqueda dio un resultado, utilizando la estructura de controlo selectivo desplegamos la información del producto y si no hay ninguna coincidencia la función simplemente desplegara un mensaje negando la busqueda. 

Eliminar producto



