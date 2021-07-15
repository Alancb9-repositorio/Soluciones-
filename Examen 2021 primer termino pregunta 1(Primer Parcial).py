"""Pregunta 1 50 pts
Asuma que tiene los siguientes diccionarios donde las claves son nombres de
artículos de una tienda y los valores corresponden a sus categorías, precios y
características:
"""
d_categorias = {
    "Ping pong":"Juego salon",
    "Scooter electrico":"Vehiculos",
    "Futbolin":"Juego salon",
    "Barbie Cantante":"Muñecas",
    "Barbie oficinista":"Muñecas",
    }
d_precios = {
    "Ping pong":230,
    "Scooter electrico":300,
    "Futbolin":70,
    "Barbie Cantante":29,
    "Barbie oficinista":30,
    }
d_caracteristicas = {
    "Ping pong":{"deporte","equipos","concentración","brazos",...},
    "Scooter electrico":{"equilibrio","deporte","individual","electrico",...},
    "Futbolin":{"equipos","brazos",...},
    "Barbie Cantante":{"muñeca","artista","individual",...},
    "Barbie oficinista":{"individual","muñeca", "electrico",...},
    }

"""Implemente las siguientes funciones:
1.[10 puntos] mas_caro(d_categorias, d_precios, categoria) que
recibe los diccionarios de categorías y precios, y un string con el
nombre de una categoría válida. La función retorna el nombre del
artículo más caro en esa categoría y su precio."""
#Solucion literal1
def mas_caro(d_categorias, d_precios, categoria):
    articulo_tienda_mayor = ""
    precio_mayor = 0
    for articulo, precio in d_precios.items():
        if precio > precio_mayor and categoria == d_categorias[articulo]:
            articulo_tienda_mayor = articulo
            precio_mayor = precio
    categoria_mayor = articulo_tienda_mayor
    return categoria_mayor
respuesta1 = mas_caro(d_categorias, d_precios, "Muñecas")
print(respuesta1)

"""2.[10 puntos] total_por_categoria(d_categorias, d_precios,
ListaCompras) que recibe los diccionarios de categorías y
precios, y una lista de strings con nombres de artículos
comprados por el usuario. La función retorna un diccionario que
indica cuánto ha gastado el usuario en cada categoría de los
artículos en la lista. Por ejemplo:

total_por_categoria(d_categorias, d_precios, ["Barbie oficinista","Ping
pong","Futbolin", "Barbie cantante"])
devuelve {"Juego salon":300, "Muñecas":59}"""
#Solucion literal 2
def total_por_categoria(d_categorias, d_precios, ListaCompras):
    d = {}
    for articulo in ListaCompras:
        d[d_categorias[articulo]] = d.get(d_categorias[articulo], 0) + d_precios[articulo]
    return d
respuesta2 = total_por_categoria(d_categorias, d_precios, ["Barbie oficinista","Pingpong","Futbolin", "Barbie cantante"])
print(respuesta2)

"""Luego, en su programa principal use las funciones previamente
implementadas donde aplique para desarrollar lo siguiente:
3. [10 puntos] Pida al usuario que ingrese varias categorías a
consultar. El usuario podrá ingresar cuántas categorías desee,
pero una a la vez; para terminar de ingresar las categorías debe
escribir la palabra "dattebayo". Para cada categoría ingresada
por el usuario muestre cuál es el artículo más caro de esa
categoría."""
#Solucion literal 3
categoria_usuario = ""
while categoria_usuario != "dattebayo":
    categoria_usuario = input("Ingrese la categoria (Si no desea ingresar mas categorias escriba dattebayo): ")
    if categoria_usuario != "dattebayo":
        articulo_mas_caro = mas_caro(d_categorias, d_precios, categoria_usuario)
        print("Para la categoria {} el articulo mas caro es: {}".format(categoria_usuario, articulo_mas_caro))
print("Gracias por consultar!")

"""4. [10 puntos] El usuario quiere comprar los siguientes artículos:
"bandana", "ramen" y "ropa akatsuki". Muestre por pantalla el
total a pagar por cada categoría de los elementos de la lista de
compras. Muestre también el total a pagar de toda la compra."""
#Solucion literal 4
diccionario = total_por_categoria(d_categorias, d_precios, ["bandana","ramen","ropa akatsuki"])
for categoria, total in diccionario.items():
    print("El total de {} es: {}".format(categoria, total))
print("El total a pagar de toda la compra es: {}".format(sum(list(diccionario.values()))))

"""5. [10 puntos] Para la siguiente lista de características
"importado", "eléctrico" y "plástico" muestre todos los artículos
que tienen al menos todas estas características en común."""
for articulo, conjunto_caracteristicas in d_caracteristicas.items():
    if ("importado" in conjunto_caracteristicas) and ("eléctrico" in conjunto_caracteristicas) and ("plástico" in conjunto_caracteristicas):
        print(articulo)






















"""
2.[10 puntos] total_por_categoria(d_categorias, d_precios,
ListaCompras) que recibe los diccionarios de categorías y
precios, y una lista de strings con nombres de artículos
comprados por el usuario. La función retorna un diccionario que
indica cuánto ha gastado el usuario en cada categoría de los
artículos en la lista. Por ejemplo:

total_por_categoria(d_categorias, d_precios, ["Barbie oficinista","Ping
pong","Futbolin", "Barbie cantante"])
devuelve {"Juego salon":300, "Muñecas":59}

Luego, en su programa principal use las funciones previamente
implementadas donde aplique para desarrollar lo siguiente:
3. [10 puntos] Pida al usuario que ingrese varias categorías a
consultar. El usuario podrá ingresar cuántas categorías desee,
pero una a la vez; para terminar de ingresar las categorías debe
escribir la palabra "dattebayo". Para cada categoría ingresada
por el usuario muestre cuál es el artículo más caro de esa
categoría.
4. [10 puntos] El usuario quiere comprar los siguientes artículos:
"bandana", "ramen" y "ropa akatsuki". Muestre por pantalla el
total a pagar por cada categoría de los elementos de la lista de
compras. Muestre también el total a pagar de toda la compra.
5. [10 puntos] Para la siguiente lista de características
"importado", "eléctrico" y "plástico" muestre todos los artículos
que tienen al menos todas estas características en común."""

"""Pregunta 2 50 pts
Asuma que tiene las siguientes tres listas paralelas:"""

l_palabras = ["hola", "futbol", "Ecuador", "Peru"]
l_categorías = ["saludo", "deportes", "paises", "paises"]
l_puntos = [5, 10, 90, 90]
