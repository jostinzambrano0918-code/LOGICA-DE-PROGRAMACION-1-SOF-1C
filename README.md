# LOGICA-DE-PROGRAMACION-1-SOF-1C


Nombre: Justin zambrano

Año: 2026-2027


Ingeniera:Monica Patricia Salazar Tapia


Tareas y proyectos.

El programa que escogí fue el popular juego de Piedra, Papel o Tijera.

Problema: crear un sistema que gestione las partidas, valide las elecciones del jugador y la computadora, lleve el puntaje y determine automáticamente cuándo el jugador gana o pierde el juego.

Este proyecto tiene como objetivo desarrollar una lógica sencilla y eficiente para comprender el funcionamiento de un programa interactivo. No busca crear un videojuego profesional ni un motor gráfico, sino aplicar los conocimientos adquiridos en clase mediante el lenguaje de programación Python, reforzando conceptos como variables, estructuras condicionales, ciclos, listas y generación de datos aleatorios.

El programa está diseñado para que el usuario interactúe mediante la consola, donde podrá seleccionar entre piedra, papel o tijera. Posteriormente, la computadora generará una elección aleatoria y el programa comparará ambas opciones para determinar el resultado de cada ronda.

La arquitectura del programa toma en cuenta al usuario como el principal actor del sistema, quien ingresa sus decisiones mediante el teclado. A partir de esta información, el programa procesa los datos, determina si existe una victoria, derrota o empate y actualiza el marcador. Además, controla el número de intentos disponibles y verifica si el jugador ha conseguido las tres victorias consecutivas necesarias para ganar la partida.

Código:

En primer lugar, se importó la librería random, la cual permite que la computadora realice una selección aleatoria entre las opciones disponibles: piedra, papel o tijera.

Posteriormente, se definieron las variables necesarias para almacenar las victorias consecutivas del jugador, el número de intentos realizados y la lista de opciones del juego.

Se implementó un ciclo while para controlar el desarrollo de la partida hasta que el jugador consiguiera tres victorias consecutivas o agotara el límite de tres intentos.

Dentro del ciclo, el programa solicita la elección del jugador y genera automáticamente la elección de la computadora utilizando una función aleatoria.

Después, mediante una estructura condicional if, elif y else, se comparan ambas elecciones para determinar si el resultado corresponde a una victoria, una derrota o un empate. Cuando el jugador gana una ronda, aumenta el contador de victorias consecutivas; en cambio, si pierde o empata, la racha de victorias se reinicia.

Finalmente, el programa verifica si el jugador logró las tres victorias consecutivas antes de finalizar los tres intentos. En caso afirmativo, muestra un mensaje indicando que el jugador ganó la partida; de lo contrario, informa que perdió el juego. Al terminar, el sistema ofrece la opción de iniciar una nueva partida o salir del programa.

Reflexión:

La programación permite resolver problemas mediante algoritmos claros y organizados. En este proyecto fue posible representar el funcionamiento de un juego clásico utilizando estructuras básicas de Python, fortaleciendo el razonamiento lógico y la capacidad para diseñar soluciones informáticas.

Herramientas como Python y Visual Studio Code facilitan el desarrollo y la prueba de programas de manera eficiente. Además, este ejercicio demuestra cómo, a partir de una lógica sencilla, es posible construir aplicaciones interactivas que posteriormente podrían evolucionar hacia videojuegos con interfaces gráficas utilizando motores como Unity o bibliotecas especializadas para Python.
