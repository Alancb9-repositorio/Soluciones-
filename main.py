import numpy as np
def cargarInfo(nombreArchivo):
    d = {}
    f = open(nombreArchivo, "r")
    for line in f:  #line = "1;(0,0),(1,0),(2,0)\n"
        l = []
        clave, coordenadas = line.strip().split(";")#["1", "(0,0),(1,0),(2,0)"]   #clave =  "1" coordenadas = "(0,0),(1,0),(2,0)".strip(")") = "(0,0),(1,0),(2,0".split("),")

        #coordenadas += ","  #coordenadas = "(0,0),(1,0),(2,0),"
        coordenadas = coordenadas.strip(")").split("),")          #["(0,0", "(1,0", "(2,0"]    
        for elemento in coordenadas:    #"(0,0".strip("(") = "0,0"[0] = int("0") = 0
            tupla_coordenada = (int(elemento.strip("(")[0]), int(elemento.strip("(")[2]))         #"0,0"----("0", "0")---(0,0)
            l.append(tupla_coordenada)
        d[int(clave)] = l
    f.close()
    return d
print(cargarInfo("coordenadas.txt"))


def colocarEnTablero(tablero, posF, posC, caracter):
    dicc = cargarInfo("coordenadas.txt")
    lista_coor_caracter = dicc[caracter]
    num_fila, num_columna = tablero.shape
    for tupla_coord in lista_coor_caracter:
        tupla_coord = list(tupla_coord)
        tupla_coord[0] += posF
        tupla_coord[1] += posC
        if tupla_coord[0] > num_fila - 1 or tupla_coord[1] > num_columna - 1:
            return -2
        elif tablero[tupla_coord[0], tupla_coord[1]] != 0:
            return -1
        else:
            tablero[tupla_coord[0], tupla_coord[1]] = caracter
    print(tablero)
    return 1
tablero = np.zeros((8,6), dtype= int)
valor = colocarEnTablero(tablero, 0, 4, 2)
print(valor)
    

from random import randint
def desordena(n):
    matriz = np.zeros((n, n), dtype = int)
    l = []
    for i in range(n):
        for j in range(n):
            num_aleatorio = randint(0, (n ** 2) - 1)
            while num_aleatorio in l:
                num_aleatorio = randint(0, (n ** 2) - 1)
            l.append(num_aleatorio)
            matriz[i, j] = num_aleatorio
    return matriz

def ubica1(matriz,k):
    return np.array([np.where(matriz == k)[0][0], np.where(matriz == k)[1][0]])

def ubica2(matriz, k):
    fila, columna = matriz.shape
    for i in range(fila):
        for j in range(columna):
            if matriz[i, j] == k:
                return np.array([i, j])
tamano = int(input("¿Tamaño del tablero?: "))
matriz = desordena(tamano)
# print(matriz)
# resultado = np.sort(np.reshape(matriz, (1, matriz.size))) + 1
# resultado[0, -1] = 0
# recorte = resultado[0, :]
# matriz_resultado = np.reshape(recorte, (tamano, tamano))
# print(matriz_resultado)
turno = 1
#print(matriz != matriz_resultado)
while np.any(matriz != matriz_resultado):
    print("Turno: {}".format(turno))
    turno += 1
    print(matriz)
    ficha = int(input("¿Ficha a mover?: "))
    num_fila, num_columna = ubica1(matriz, ficha)    #([#f, #c])
    vector_fila = matriz[num_fila, :]
    vector_columna = matriz[:, num_columna]
    if (0 in vector_fila) or (0 in vector_columna):
        ubicacion_cero_fila, ubicacion_cero_colum = ubica1(matriz, 0)  #([#f, #c])
        matriz[ubicacion_cero_fila, ubicacion_cero_colum] = ficha
        matriz[num_fila, num_columna] = 0
    else:
        print("No se pudo realizar el intercambio")
 print("FELICIDADES GANASTE CRACK")
print("Te tomo {} turnos".format(turno))