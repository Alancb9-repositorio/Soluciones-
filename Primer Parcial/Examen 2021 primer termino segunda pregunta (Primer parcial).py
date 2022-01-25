"""Pregunta 2 50 pts
Asuma que tiene las siguientes tres listas paralelas:"""

l_palabras = ["hola", "futbol", "Ecuador", "Peru",...]
l_categorías = ["saludo", "deportes", "paises", "paises",...]
l_puntos = [5, 10, 90, 90, ...]

"""1. [10 puntos] Implemente la función desordenar(palabra) que recibe
una palabra y la retorna desordenada. Para desordenar, la función
toma aleatoriamente dos índices distintos de la palabra e intercambia
las letras en esos índices. Repita este proceso 5 veces."""
#Solucion literal 1
from random import randint
def desordenar(palabra):
    lista_palabra = list(palabra)
    for i in range(5):
        indice_1 = randint(0, len(lista_palabra) - 1)
        indice_2 = randint(0, len(lista_palabra) - 1)
        while indice_2 == indice_1:
            indice_2 = randint(0, len(lista_palabra) - 1)
        letra1 = lista_palabra[indice_1]
        letra2 = lista_palabra[indice_2]
        lista_palabra[indice_1] = letra2
        lista_palabra[indice_2] = letra1
    return "".join(lista_palabra)
respuesta = desordenar("futbol")
print(respuesta)

"""2. [35 puntos] Luego implemente un juego de adivinar palabras
usando la siguiente mecánica:
A. El usuario debe escoger una categoría de juego (ingreso por
teclado).
B. Su programa debe crear dos nuevas listas paralelas (palabras
y puntos) considerando solamente las palabras de esa categoría.
En cada iteración del juego (turno):
C. Su programa escoge una palabra aleatoria para jugar y luego
la desordena utilizando la función desordenar.
D. Muestre al jugador la palabra desordenada y pídale que la
adivine (ingreso por teclado)
E. Si adivina, el jugador acumula los puntos de la palabra
multiplicados por la longitud de la misma. En caso contrario, el
jugador acumula un intento fallido. En ambos casos, se pasa al
siguiente turno y la palabra usada en este turno del juego ya
no podrá volver a aparecer en un turno posterior.
F. El juego termina cuando el usuario se ha equivocado 3 veces o
las palabras de la categoría escogida se han terminado.
3. [5 puntos] Al final muestre los puntos acumulados y las palabras
adivinadas correctamente por el jugador durante el juego
"""
#Solucion literal 2
equivocaciones = 0
longitud_categorias = len(l_palabras)
puntos_palabra = 0
palabras_adivinadas = []
while equivocaciones < 3 or longitud_categorias == 0:
    categoria_usuario = input("Estimado usuario ingrese una categoria: ").lower()
    lista_palabras = []
    lista_puntos = []
    for indice in range(len(l_categorías)):
        if l_categorías[indice] == categoria_usuario:
            lista_palabras.append(l_palabras[indice])
            lista_puntos.append(l_puntos[indice])
    palabra_aleatoria = lista_palabras[randint(0, len(lista_palabras) - 1)]
    palabra_desordenada = desordenar(palabra_aleatoria)
    print("La palabra desordenada es: {}".format(palabra_desordenada))
    palabra_adivinada = input("Intente adivinar la palabra anterior: ").lower()
    if palabra_adivinada == palabra_aleatoria:
        print("Felicidades adivinaste!")
        palabras_adivinadas.append(palabra_adivinada)
        puntos_palabra += lista_puntos[lista_palabras.index(palabra_adivinada)] * len(palabra_adivinada)
    else:
        equivocaciones += 1
    l_palabras.remove(palabra_aleatoria)
    print("SIGUIENTE TURNO")
#Solucion literal3
print("Los puntos acumulados fueron: {} pts".format(puntos_palabra))
print("Las palabras adivinadas correctamente fueron:")
for p in palabras_adivinadas:
    print(p)


