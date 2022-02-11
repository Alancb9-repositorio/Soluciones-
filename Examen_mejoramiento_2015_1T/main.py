from random import randint
import numpy as np
def llenar(n): 
    l = []
    for i in range(n):
        numero_aleatorio = randint(0, 99)
        while numero_aleatorio in l:
            numero_aleatorio = randint(0, 99)
        l.append(numero_aleatorio)
    c = l.copy()
    c.sort()
    return l, c[1]
lista, valor = llenar(10)
print(lista)
print(valor)

def tablaPosiciones (matrizGoles):
    d = {}
    num_filas, num_columnas = matrizGoles.shape #(3f, 3c)
    for indice_fila in range(num_filas):
        partidos_ganados = 0
        partidos_empatados = 0
        partidos_perdidos = 0
        equipo = indice_fila + 1
        goles_equipo = np.sum(matrizGoles[indice_fila, :])
        for indice_columna in range(num_columnas):
            if indice_fila != indice_columna:
                goles_equipo_local = matrizGoles[indice_fila, indice_columna]
                goles_equipo_visitante = matrizGoles[indice_columna, indice_fila]
                if goles_equipo_local == goles_equipo_visitante:
                    partidos_empatados += 1
                elif goles_equipo_local > goles_equipo_visitante:
                    partidos_ganados += 1
                else:
                    partidos_perdidos += 1
        d[equipo] = [partidos_ganados, partidos_empatados, partidos_perdidos]
    return d
m = np.array([[0,2,1,3],
             [2,0,2,1],
             [3,2,0,1],
             [4,1,2,0]])
a = tablaPosiciones(m)
print(a)

def ganador(diccPosiciones):
    lista_equipos = []
    lista_puntajes = []
    for equipo, lista_estadisticas in diccPosiciones.items():
        partidos_ganados = lista_estadisticas[0]
        partidos_empatados = lista_estadisticas[1]
        partidos_perdidos = lista_estadisticas[2]
        puntaje = (partidos_ganados * 3) + (partidos_empatados * 1)
        lista_equipos.append(equipo)
        lista_puntajes.append(puntaje)
    indice_max = lista_puntajes.index(max(lista_puntajes))
    equipo_ganador = lista_equipos[indice_max]
    return equipo_ganador
print(ganador(a))