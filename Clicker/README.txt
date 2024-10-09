Bubble Blitz
Bubble Blitz es un juego casual en el que debes hacer clic en las burbujas
o presionar las letras asignadas en tu tecladopara explotarlas.
A medida que avances, las burbujas aparecerán con mayor velocidad,
poniendo a prueba tus reflejos y tu capacidad de reaccionar tanto con el mouse como con el teclado.
¡Tu objetivo es obtener la mayor puntuación posible en 2 minutos!



Descripción General
En Bubble Blitz, deberás interactuar con burbujas de diferentes colores y tamaños que aparecen en pantalla.
Puedes hacer clic en ellas para explotarlas o, si tienen una letra asignada,
presionar esa letra en tu teclado para eliminarlas.
A lo largo del juego, la velocidad y dificultad aumentarán gradualmente,
desafiándote a mejorar tu precisión.


Requisitos Previos:

Antes de jugar, necesitas tener instalado el paquete Pygame.
Para instalarlo, ejecuta el siguiente comando en tu terminal:
pip install pygame


Instalación y Ejecución:
Clona este repositorio o descarga los archivos del juego.
Asegúrate de tener Pygame instalado.
Ejecuta el archivo principal del juego desde la terminal con:
python main.py
¡Y estarás listo para jugar!


Controles:
Mouse: Haz clic en las burbujas para explotarlas.
Teclado (letras a,b,c,d,e,f): Presiona la letra asignada a la burbuja para explotarla.

Objetivo del Juego:
El objetivo es conseguir la mayor puntuación posible en un tiempo límite de 2 minutos.
Cada burbuja explotada te da puntos, ¡así que trata de no dejar escapar ninguna!


Nivel y Dificultad:
El juego tiene un único nivel con dificultad ajustada entre fácil y media, lo que lo hace accesible pero desafiante para mejorar tu puntuación.


Autor
Kaleb Fuentes Puello
Correo: krfpdev@gmail.com
Teléfono: +573005271964


********************************* Detalles Tecnicos *************************************
Descripción de los archivos:

main.py: Este archivo contiene la lógica principal del juego.
Define la pantalla, los sonidos, el fondo, y el menú.
El bucle principal del juego se encuentra aquí, junto con la gestión del tiempo,
el sistema de puntos y la interacción con las pelotas, ya sea mediante clics del mouse o la pulsación de teclas.
También incluye funciones para dibujar el menú y manejar el cierre del juego correctamente.


constantes.py: Este archivo almacena todas las constantes utilizadas en el juego,
como el tamaño de la pantalla, los colores de las pelotas y la tasa de cuadros por segundo (FPS).
También contiene una lista de colores que se usan para las pelotas generadas aleatoriamente.


pelota.py: Define la clase Pelota, que gestiona las burbujas que aparecen en el juego.
Cada burbuja puede ser clickeada o explotar con una tecla asignada.
También maneja el movimiento de las pelotas, la detección de colisiones,
y la generación de fragmentos cuando una pelota explota.


fragmento.py: Este archivo contiene la clase Fragmento,
que define los pequeños fragmentos que se generan cuando una pelota explota.
Cada fragmento se mueve en direcciones aleatorias y se dibuja en la pantalla por un tiempo limitado.

