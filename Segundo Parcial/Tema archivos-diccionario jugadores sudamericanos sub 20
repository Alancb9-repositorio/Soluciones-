"""Tema2. (60 puntos) Asuma que tiene un archivo por cada partido jugado en el Sudamericano Sub-20.
 Cada archivo tiene información con datos de los jugadores que participaron en el partido con el siguiente formato:
 
 Ejemplo:
Pais,Jugador,Tarjetas_Amarillas,Tarjetas_Rojas,Goles,Minutos,KM_recorridos
...
Ecuador,Jose Cifuentes,1,0,0,75,6.3
Uruguay,Sebastian Caceres,2,1,0,90,7
Ecuador,Leonardo Campana,0,0,1,87,10
...

Implemente las siguientes funciones:

1.  actualizaDiccionario(nomArchivo,dic) que recibe el nombre de un archivo con los datos del partido
y actualiza el diccionario de totales por jugador que tiene el siguiente formato:

dic = {'Ecuador': {'Leonardo Campana': {'TA': 0,
                                        'TR': 0,
                                        'Goles': 1,
                                        'Minutos': 87,
                                        'KM': 10.0}},
       'Uruguay': {'Sebastian Caceres': {'TA': 2,
                                         'TR': 1,
                                         'Goles': 0,
                                         'Minutos': 90,
                                         'KM': 7.0}
                   }
       }

2. buenDeportista(jugador, dic) que recibe el nombre de un jugador y el diccionario de totales y determina
si ese jugador puede ser catalogado como un «buen deportista»; la función retorna «True» o «False» .
Un jugador se considera «buen deportista»si ha recibido menos de dos tarjetas por cada 270 minutos de juego.

3.JugadorAtleta(jugador,dic) que recibe el nombre de un jugador y el diccionario de totales, determinando si
el jugador ha corrido como mínimo el promedio de lo que han corrido los jugadores de su pais y ha anotado
al menos un gol; la función retorna «True» o «False»

4. paisBuenasPracicas(pais,dic) que recibe el nombre de un país y el diccionario de totales, analizando si ese
país puede ser nominado para el «Best Practices award». Un país puede ser nominado a este premio si TODOS los 
jugadores del país pueden ser catalogados como «buen deportista». La funcion retorna «True»o «False»

Escriba un programa que:
5. Forme el diccionario de totales a partir de una lista con los nombres de los archivos de datos de los partidos. 
Asuma que tiene una lista para esta tarea:

L = ['br-ur.csv', ...,'ec-vn.csv']

6. Muestre los siguiente datos por país:
a. Porcentaje de jugadores atletas. es decir e número de jugadores atletas dividido para el total de jugadores del país.
b. Goles por Km recorrido, es decir el número de goles del país dividido para el total de Km recorridos por todos sus jugadores

7. Muestre los países nominados para el «Best Practices award

8 Muestre la nómina de jugadores atletas con su respectivo país.

 """
#Solucion
"""EJERCICIO 1"""
def actualizaDiccionario(nomArchivo, dic):
    f = open(nomArchivo, "r")
    for line in f:
        info_jugadores = line.strip().split(",")     #[Nombrepais,nombrejugador,ta,tr,goles,min,km]
        dic[info_jugadores[0]] = dic.get(info_jugadores[0], {})
        dic[info_jugadores[0]][info_jugadores[1]] = dic[info_jugadores[0]].get(info_jugadores[1], {})
        for indice in range(len(info_jugadores)):
            if indice == 2:
                dic[info_jugadores[0]][info_jugadores[1]]["TA"] = dic[info_jugadores[0]][info_jugadores[1]].get("TA", 0) + int(info_jugadores[indice])
            elif indice == 3:
                dic[info_jugadores[0]][info_jugadores[1]]["TR"] = dic[info_jugadores[0]][info_jugadores[1]].get("TR", 0) + int(info_jugadores[indice])
            elif indice == 4:
                dic[info_jugadores[0]][info_jugadores[1]]["Goles"] = dic[info_jugadores[0]][info_jugadores[1]].get("Goles", 0) + int(info_jugadores[indice])
            elif indice == 5:
                dic[info_jugadores[0]][info_jugadores[1]]["Minutos"] = dic[info_jugadores[0]][info_jugadores[1]].get("Minutos", 0) + int(info_jugadores[indice])
            elif indice == 6:
                dic[info_jugadores[0]][info_jugadores[1]]["KM"] = dic[info_jugadores[0]][info_jugadores[1]].get("KM", 0) + float(info_jugadores[indice])
    f.close()

d = {}
actualizaDiccionario("Partidos Sub-20", d)
print(d)

"""EJERCICIO 2"""
def buenDeportista(jugador, dic):
    for pais, diccionario_jugadores in dic.items():
        for jugador1, diccionario_datos in diccionario_jugadores.items():
            if jugador == jugador1:
                tarjeta_amarilla = diccionario_datos["TA"]
                tarjeta_roja = diccionario_datos["TR"]
                total_tarjetas = tarjeta_amarilla + tarjeta_roja
                division_minutos = diccionario_datos["Minutos"] // 270
                return total_tarjetas <= division_minutos

resultado = buenDeportista("Jose Cifuentes", d)
print(resultado)

"""EJERCICIO 3"""
def JugadorAtleta(jugador, dic):
    suma_kilometros = 0
    for pais, d_jugadores in dic.items():
        if jugador in d_jugadores:
            cant_jugadores = len(list(d_jugadores.keys()))
            for datos in d_jugadores.values():
                kilometros = datos["KM"]
                suma_kilometros += kilometros
            promedio = suma_kilometros / cant_jugadores
            print(promedio)
            kilometros_jugador = d_jugadores[jugador]["KM"]
            print(kilometros_jugador)
            cant_goles = d_jugadores[jugador]["Goles"]
            return (kilometros_jugador >= promedio) and (cant_goles >= 1)

resultado = JugadorAtleta("Sebastian Caceres", d)
print(resultado)

"""EJERCICIO 4"""
def paisBuenasPracticas(pais, dic):
    for clave_pais, dic_jugador in dic.items():
        if clave_pais == pais:
            cant_buen_jugador = 0
            for jugador in dic_jugador:
                buen_jugador = JugadorAtleta(jugador, dic)
                cant_buen_jugador += buen_jugador
            return cant_buen_jugador == len(list(dic_jugador.keys()))

result = paisBuenasPracticas("Ecuador", d)
print(result)

"""EJERCICIO 5"""
L = ['br-ur.csv', ...,'ec-vn.csv']
d = {}
for archivo in L:
    actualizaDiccionario(archivo, d)

"""EJERCICIO 6
Literal a"""
for pais, dic_jugadores in d.items():
    cant_jugadores = len(list(dic_jugadores.values()))
    cant_buenos_jugadores = 0
    for jugador, datos in dic_jugadores.items():
        buen_jugador = JugadorAtleta(jugador, d)
        cant_buenos_jugadores += buen_jugador
    porcentaje = cant_buenos_jugadores * 100 / cant_jugadores
    print(porcentaje)
"""Literal b"""
for pais, dic_jugadores in d.items():
    total_goles = 0
    total_kilometros = 0
    for jugador, dic_datos in dic_jugadores.items():
        num_goles = dic_datos["Goles"]
        total_goles += num_goles
        kilometros = dic_datos["KM"]
        total_kilometros += kilometros
    goles_kilometro = total_goles / total_kilometros
    print(goles_kilometro)

"""EJERCICIO 7"""
for pais in d:
    buen_pais = paisBuenasPracticas(pais, d)
    if buen_pais:
        print(pais)

"""EJERCICIO 8"""
for pais, dic_jugadores in d.items():
    print(pais)
    for jugador in dic_jugadores:
        jugador_atleta = JugadorAtleta(jugador, d)
        if jugador_atleta:
            print(jugador)
