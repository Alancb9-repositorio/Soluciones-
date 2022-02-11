from random import randint
def asignarPosicionElementos():
    armas = [0] * 50
    viveres = [0] * 50
    tesoros = [0] * 50
    for i in range(8):
        pos_armas = randint(1, 49)
        while armas[pos_armas] == 1 or viveres[pos_armas] == 2 or tesoros[pos_armas] == 3:
            pos_armas = randint(1, 49)
        armas[pos_armas] = 1
        pos_viveres = randint(1, 49)
        while armas[pos_viveres] == 1 or viveres[pos_viveres] == 2 or tesoros[pos_viveres] == 3:
            pos_viveres = randint(1, 49)
        viveres[pos_viveres] = 2
        pos_tesoros = randint(1, 49)
        while armas[pos_tesoros] == 1 or viveres[pos_tesoros] == 2 or tesoros[pos_tesoros] == 3:
            pos_tesoros = randint(1, 49)
        tesoros[pos_tesoros] = 3
    return armas, viveres, tesoros


print(armas)
print(viveres)
print(tesoros)

def lanzarDado():
    return randint(1, 6)

def generarEstado():
    return randint(-3, -1)

def mostrarElemento(posicion, coleccion):
    tipo_elemento = coleccion[posicion]
    if tipo_elemento == 1:
        print("El elemento es un arma")
    elif tipo_elemento == 2:
        print("El elemento es un vivere")
    elif tipo_elemento == 3:
        print("El elemento es un tesoro")
    else:
        print("No existe elemento alguno en esta posicion")

def recogerElemento(estado, posicion,coleccion):
    tipo_elemento = coleccion[posicion]
    if tipo_elemento == 1 and estado == -1:
        return tipo_elemento
    elif tipo_elemento == 2 and estado == -2:
        return tipo_elemento
    elif tipo_elemento == 3 and estado == -3:
        return tipo_elemento
    else:
        return 0

def mostrarMensaje(jugador, estado, posicion):
    print("El jugador {} esta en la posicion {} en un estado de {}".format(jugador, posicion, estado))

def  calcularRiqueza(armas,viveres,tesoros):
    return (((armas/2) + 1) * 100) + (0.5 * viveres) + tesoros


