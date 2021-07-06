"""El juego de mesa Scrabble es un juego donde se forman palabras en un tablero, a las cuales se les 
asigna un puntaje. Las palabras pueden crearse cruzándolas con palabras ya existentes en el tablero. El 
ganador es quien más puntos haya obtenido:"""
"""Las letras compartidas entre palabras reciben el doble de puntos. Su programa recibirá una secuencia 
de palabras, separadas por comas, ingresada por el usuario por teclado y determinará el puntaje de 
cada una. Para denotar una letra compartida, la misma será sucedida por el símbolo “*”. Asuma que 
todas las palabras terminan con una letra compartida. Todas las letras ingresadas deben ser 
mayúsculas. Si se ingresa un letra minúscula, esta es ignorada (puntuación de 0 para dicha letra). 
Finalmente, se debe determinar la palabra con mayor puntaje.
Una corrida ejemplo del programa sería:

Ingrese las palabras a calificar: CAS*A*,S*ASTR*E*,R*EY*,A*ZOTE* 
Las calificaciones de las palabras son:
casa: 8 
sastre: 9 
rey: 11 
azote: 16
La palabra con mayor puntaje es AZOTE (16 puntos).

Detalle de cómo se obtuvieron los puntajes de cada palabra:
String ingresado: CAS*A*,S*ASTR*E*,R*EY*,A*ZOTE*
casa: 8 -> 3 + 1 + (2 * 1) + (2 * 1)
sastre: 9 -> (2 * 1) + 1 + 1 + 1 + (2 * 1) + (2 * 1)
rey: 11 -> (2 * 1) + 1 + (2 * 4)
azote: 16 -> (2 * 1) + 10 + 1 + 1 + (2 * 1)
"""
puntaje_letras = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2, 'H':4, 'I':1,
                'J':9, 'K':5, 'L':1, 'M':3, 'N':1,'O':1, 'P':3, 'Q':10,'R':1,
                'S':1, 'T':1, 'U':1, 'V':4, 'W':4,'X':9, 'Y':4, 'Z':10}
frase = input("Ingrese las palabras a calificar: ")
lista_de_palabras = frase.split(",")
d = {} #{"palabra": puntaje,...}
for palabra in lista_de_palabras:
    palabra_limpia = ""
    valor_letra = 0
    for indice in range(len(palabra)):
        if palabra[indice] != "*" and palabra[indice].isupper():
            valor_letra = puntaje_letras[palabra[indice]]
            if palabra[indice + 1] == "*":
                valor_letra = valor_letra * 2
            palabra_limpia += palabra[indice]
    d[palabra_limpia] = d.get(palabra_limpia, 0) + valor_letra
print("Las calificaciones de las palabras son: ")
for palabra, puntaje in d.items():
    print("{}: {}".format(palabra, puntaje))
l_palabras = []
l_puntajes = []
for clave, valor in d.items():
    l_palabras.append(clave)
    l_puntajes.append(valor)
puntaje_maximo = max(l_puntajes)
indice_maximo = l_puntajes.index(puntaje_maximo)
palabra_maxima = l_palabras[indice_maximo]
print("La palabra con mayor puntaje es {}({} puntos)".format(palabra_maxima, puntaje_maximo))