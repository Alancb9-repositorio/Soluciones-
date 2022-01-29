[TEMA 1 50 PUNTOS]Para el Atlántico Norte, los meteorólogos registran los parámetros que describen a los huracanes .

La tabla muestra los datos en una matriz M para cada año y nombre asignado al huracan:

El encabezado de la matriz se describe en el diccionario huracanes que contiene el año (clave tipo entero)
y los nombres  de huracanes en ese año (texto en tupla).

huracanes = {..., 
             2015:('Ana', ..., 'Kate'),
             2016:('Alex', ..., 'Otto'),
             2017:('Ariene', ..., 'Harvey','Irma', ...), 
             ... }

Los nombres no se repiten y se almacenan en el mismo orden que en la matriz M.

Por la velocidad del viento, los huracanes se categorízan en :

categoria	Velocidad del Viento
1	         menor a 100 km/h
2	         100 a 150 km/h
3	         150 a 200 km/h
4	         200 a 250 km/h
5	         mas de 250 km/h

Desarrolle los siguientes literales:

a) Elabore la función total_marejada(M, cat) que retorna el total de marejadas en metros causadas por los huracanes que tengan categoria cat.

b) Implemente la función indices_año(huracanes, año) que retorna una tupla con los índices de columna donde empieza y termina año en la matriz M.

c) Escriba la función velocidad_superior(M, huracanes, año) que retorna la cantidad de huracanes en año que tienen la Velocidad de Desplazamiento (Vd) superior a la Velocidad de Desplazamiento promedio del año dado como parámetro.

d)  Realice la función ACE(M, huracanes, año) que devuelve la cantidad de energía liberada por todos los huracanes de la temporada año.
Esto se calcula usando:

Donde VVi es la Velocidad de Viento (en km/h) de cada huracan.

e) Implemente la función lluvia(M, huracanes, nombre_huracan, año) que devuelve la cantidad de lluvia en centímetros (cm) generada por el nombre_huracan en ese año.

ejemplo:
M = np.array([[20, 30, 19, 15, 18],
              [89,195,120,150,240],
              [65,165,100,110,200],
              [30, 49, 35, 89, 67],
              [ 5, 1.8,  1,  2,  5]])

huracanes = {2016:('Alex', 'Otto'),
             2017:('Ariene', 'Harvey','Irma'),
             }
Se obtiene:
---
categorias:  [1 3 2 2 4]
Marejadas cat[2]:  3.0
indices:  [2, 4]
velocidad superior:  2
Energia liberada:  0.091
lluvia en mm:  89.0


[TEMA 2 40 PUNTOS]En una empresa de transporte de carga (trailers) se registran para cada fecha,
el código de  los choferes que manejaron en una ruta.

El registro genera un archivo "rutasManejadas2018.txt" en el formato mostrado:
 
id_ruta, id_chofer, fecha
Guayaquil-Cuenca,SMS,17-05-2018
Guayaquil-Cuenca,AGB,18-05-2018
Guayaquil-Cuenca,SMZ,17-05-2018
Guayaquil-Daule,EVN,17-05-2018
Guayaquil-Daule,AAQ,18-05-2018

Por lo rutinario del trabajo, se ha recomendado que los choferes no repitan una ruta
para los últimos n días a partir de una fecha. 
Para seguir la recomendación se requiere implementar:

a) La función cargarDatos(narchivo) que recibe un archivo de registro y retorna una tupla con:
– un conjunto con los choferes que trabajaron en las fechas  del archivo (id_chofer)
– los datos del archivo en un diccionario con la estructura mostrada.

{'17-05-2018': {'Guayaquil-Cuenca': ['SMS', 'SMZ', ...],
                'Guayaquil-Daule': ['EVN', ...]},
 '18-05-2018': {'Guayaquil-Cuenca': ['AGB', ...],
                'Guayaquil-Daule': ['AAQ', ...]}}

b) La función encontrarChoferes(datos, loschoferes, unafecha, unaruta, n),  que para seguir la recomendación,
encuentra aquellos choferes que no manejaron en una ruta, durante los n dias anteriores a una fecha.

c) La función grabarArchivo(datos, loschoferes, unafecha, unaruta, n) que crea un archivo
con el resultado de la función anterior con el formato mostrado.
El nombre del archico generado se conforma como: «unaruta_unafecha.txt»

Nombre de archivo: Guayaquil-Cuenca_19-05-2018_2.txt

Para la ruta Guayaquil-Cuenca los choferes disponibles para la fecha 19-05-2018 que no hayan manejado 2 dias anteriores son: 
EVN
AAQ

d) Genere todos los archivos para todas las rutas disponibles.

NOTA: Para administrar las fechas, usted ya dispone de una función calcularFecha(unafecha,n)
que recibe una fecha y los n días anteriores y determina la fecha pasada. El formato de fecha se maneja en el mismo
formato de fecha que el archivo.

>>> calcularFecha('19-05-2018',2)
'17-05-2018'

[TEMA 3 10 PUNTOS]
Analice el código fuente de los programas que se muestran a continuación. Seleccione la respuesta correcta y justifique brevemente su respuesta.
1. [3 PUNTOS]Determine la salida por pantalla del siguiente código:

X = 2
y = 5
z = x + z
print("La suma es ,z")

a. Error: La variable z no ha sido definida
b. La suma es ,z
c. Error: La variable z no se ha inicializado
d. La suma es 7

2. [3 PUNTOS]Dado el siguiente segmento de código y las listas A y B, seleccione correctamente la salida por pantalla:

A = [3, 2, 7, 5] 
B = [31, 5, 4, 8, 12, 3, -9, 6] 
C = 0 
N = 3 
for i in range(0, 4) :
    B[A[i]] = B[A[i]] + N 
    C += B[A[i]] 
print(C)

a. 27
b. 33
c. 6
d. Ninguna de las anteriores

3. [4 PUNTOS]Dado el programa descrito a continuación, indique la salida y justifique su respuesta:

import numpy as np

L = [10,12,11,4,8]
M = [4,2,1,2,7]

matriz = np.array([],int)
A = np.append(matriz,L[2:4])
B = np.append(A,M[1:3]).reshape((2,2))
C = (A * B)//2

print(C)


