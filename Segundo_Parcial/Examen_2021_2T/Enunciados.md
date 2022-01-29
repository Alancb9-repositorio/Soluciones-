Usted es analista en una compañia que distribuye peliculas en diferentes ciudades del mundo.

Para su analisis cuenta con un diccionario de peliculas vistas por ciudades donde las claves son los nombres de las ciudades y los valores son listas con los nombres de todas las peliculas vistas en cada ciudad.

Ejemplo del diccionario de peliculas por ciudad:

dic_peliculas_ciudades = {
    "Madrid": ["Rapido y Furioso 9", "Despicable me",..],
    "Estambul": ["Jurassic Park", "Encanto",...],
    "Quito": ["Encanto", "Extincion", "Spiderman",...]
    "Moscu": ["Extincion", "Rapido y Furioso 9",...],
    "Turquia": ["Iron Man", ...],
    "Chicago": ["Encanto", "Jurassic Park",..],
    ...
}

Puede asumir que todas las ciudades han visto las mismas peliculas que su compania distribuye.

Adicionalmente asuma que tiene un diccionario con TODAS las peliculas filmadas en la historia del mundo(no todas las peliculas son distibuidas por su compañia) donde la clave es el nombre de la pelicula y el valor es una lista con los actores , actrices, director y el estudio de la pelicula. el estudio siempre sera el ultimo valor en la lista.

Ejempli del diccionario de peliculas de toda la historia:

dic_movies = {
    "Rapido y Furioso 9": ["Paul Walker", "Vin diesel", "Dwayne Johnson",...,"Universal"],
    "Despicable me": ["Gwyneth Paltrow", "Bruce Willis", ..., "Universal"],
    "Encanto": ["Stephanie Beatriz", "Jessica Darrow", "Diane Guerrero", ..., "Disney"],
    ...,
    "Spiderman": ["Tom Holland", ...., "Sony"],
    ....
}

[TEMA 1 20 PTS]
Implemente la funcion crearMatrizDta(dic_peliculas_ciudades) que recibe el diccionario de peliculas por ciudad.

Analizando el diccionario recibido, forme un vector con todas las ciudades en el diccionario(en este vector no puede haber valores repetidos). Luego, forme otro vector con todas las peliculas en el diccionario(nuevamente, no puede haber valores repetidos). estos vectores le serviran luego como sus etiquetas de filas y columnas en el programa.

Tambien, genere de manera aleatoria una matriz M de numeros enteros entre 4 y 17. Las filas de la matriz representan las ciudades(del diccionario de peliculas por ciudad), las columnas representan las peliculas(del diccionario de peliculas por ciudad), y las celdas representan el numero de semanas que la pelicula estuvo en cartelera en cada una de las ciudades.

Ayuda: Lafuncion numpy.random.randint(limite_inferior, limite_superior, (num_filas, num_columnas)) puede servir para generar una matriz de num_filas por num_columnas con valores aleatorios entre el limite_inferior y limite_superior -1.

![](Segundo_Parcial/Examen_2021_2T/matriz.jpeg){width=20 height=20}

Finalmente, la funcion retorna una tupla con los siguientes 3 valores: (1) vector de etiquetas de filas, (2) vector de etiquetas de columnas, (3) matriz de semanas de cartelera.

[TEMA 2 20 PTS]
Nota: Para resolver este ejercicio necesita utilizar tambien el diccionario dic_movies pues es el que tiene la informacion del estudio.

Implemente la funcion obtenerTop_n(matriz, v_names_filas, v_names_cols, dic_movies, n, estudio) que recibe la matriz formada en el TEMA 01 junto con los vectores de etiquetas de filas y columnas, el diccionario dic_movies, un entero n y un string que representa el nombre de un estudio. Calcule y retorne una lista con las n peliculas del estudio indicado con mas semanas TOTALES en cartelera.

Ayuda: Primero forme una lista con los nombres de todas las peliculas del estudio indicado. esto lo logra recorriendo y analizando cada uno de los elementos del diccionario dic_movies.

[TEMA 3 50 PTS]
 Este tema debe ser resuelto usando Numpy. No se permite convertir los vectores y matrices a listas u otros tipos de datos. Todo tiene que ser resuelto utilizando las funciones y conceptos vistos de numpy.

 En su programa principal realice lo siguientes:

 1.[10 puntos] Para cada pelicula en la matriz M, calcule y muestre por pantalla el nombre de la pelicula y su promedio de semanas en cartelera.

 2.[10 puntos] Identifique y muestre por pantalla el nombre de TODAS las peliculas que tuvieron MENOS semanas en cartelera en turquia que en madrid.

 3.[10 puntos] Identifique y muestre el nombre de la pelicula que tuvo MAS semanas en cartelera en Quito. Muestre tambien el nombre del estudio que produjo esa pelicula.

 4.[10 puntos] Usando la funcion del Tema 2, calcule y muestre el nombre de las 4 peliculas de estudios "Universal" con mas semanas en cartelera.

 5. [10 puntos] Identifique el promedio de semanas en cartelera para las peliculas en Moscu. Luego, muestre por pantalla los nombres de todas las peliculas en Moscu que tuvieron MAS semanas en cartelera que este promedio que calculo.

6.[TEMA 4 10 PTS]
Escriba un reporte de peliculas proyectadas en Quito en el archivo carteleraQuito.csv. El formato del archivo es el siguiente:
Pelicula|semanas en cartelera|estudio

Ejemplo:

Pelicula|semanas en cartelera|estudio
Spiderman|12|Sony
Rapidos y furiosos 9|26|Universal
...
Mi Pobre Angelito|7|TouchStone
...
Bambi|11|Disney
