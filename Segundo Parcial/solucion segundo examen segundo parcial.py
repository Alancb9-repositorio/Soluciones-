import numpy as np
dictRegiones = {}
"""Pregunta 1. Literal a, b, c, d"""
def cargar_info(nom_file, mes):
    f = open(nom_file)  #Se asume que el archivo ya viene con su extension
    vacunas = f.readline().strip().split(":")[1].split(",")
    ciudades = f.readline().strip().split(":")[1].split(",")
    poblacion = []
    for elemento in f.readline().strip().split(","):
        poblacion.append(int(elemento.split(":")[1])) #Se asume que la cantidad de poblacion es de tipo entero
    matriz = np.zeros((len(vacunas), len(ciudades)), int)
    for line in f:  #se asume que cada fila del archivo ya esta ordenado por region
        ciudad, fecha, vacunaMarcaCant = line.strip().split(";")
        if mes == int(fecha.split("-")[1]):
            for marcaVacuna_cant in vacunaMarcaCant.split("|"):
                matriz[vacunas.index(marcaVacuna_cant.split(",")[0]), ciudades.index(ciudad)] = int(marcaVacuna_cant.split(",")[1])
    f.close()            
    return np.array(poblacion), np.array(vacunas), np.array(ciudades), matriz


"""Pregunta 2"""
def total_inmunizados(nom_file, mes_inicial, mes_final):
    f = open(nom_file)
    vacunas = f.readline().strip().split(":")[1].split(",")
    ciudades = f.readline().strip().split(":")[1].split(",")
    matriz = np.zeros((len(vacunas), len(ciudades)), dtype = int)
    f.close()
    for numero_mes in range(mes_inicial, mes_final + 1): #(1,2,3,4) numero_mes = 2
        poblacion, vacunas, ciudades, matriz_info = cargar_info(nom_file, numero_mes)   #cargar_info(nom_file, 2)
        matriz = matriz + matriz_info
    return matriz

"""Pregunta 3"""
def mas_inmunizados(nom_file, mes, Num):
    poblacion, vacunas, ciudades, matriz = cargar_info(nom_file, mes)
    top_ciudades = []
    for indice, elemento in enumerate(vacunas):
        top_ciudades.append(np.array(ciudades[np.argsort(matriz[indice, :])[::-1]][:Num]))
    return tuple(top_ciudades)

"""Pregunta 4"""
def region_ciudad(dic_regiones, vec_ciudades):
    regiones = []
    for ciudad in vec_ciudades:
        for region, dic_paises in dic_regiones.items():
            for lista_ciudades in dic_paises.values():
                if ciudad in lista_ciudades:
                    regiones.append(region)
    return np.array(regiones)

"""PROGRAMA PRINCIPAL"""
"""Pregunta 5"""
total_inmunizados1 = total_inmunizados("vacunacionCovid.csv", 1, 8)

"""Pregunta 6"""
suma_inmunizados = np.sum(total_inmunizados1, axis = 0)
poblacion, vacunas, ciudades, matriz = cargar_info("vacunacionCovid.csv", 1)
resultado = ciudades[(suma_inmunizados / poblacion) > 45]
print("Las ciudades con una cantidad de inmunizados de mas del 45 son:")
for i in resultado:
    print(resultado[i])

"""Pregunta 7"""
total_inmunizados2 = total_inmunizados("vacunacionCovid.csv", 4, 6)
respuesta = suma_inmunizados[(suma_inmunizados / poblacion) > 45] - np.sum(total_inmunizados2, axis = 0)[(suma_inmunizados / poblacion) > 45]
print("La diferencia en el numero de inmunizado con respecto al literal anterior es: ")
for i in range(len(resultado)):
    print("{}: {}".format(resultado[i], respuesta[i]))

"""Pregunta 8"""
lista_regiones = ["Latinoamerica", "Norteamerica", "Europa", "Asia"]    #Ejemplo de lista
total = total_inmunizados("vacunacionCovid.csv", 1, 8)
f = open("reporte.txt", "w")
poblacion, vacunas, ciudades, matriz = cargar_info("vacunacionCovid.csv", 1)

# for region in lista_regiones:
#     f.write(region + "\n")
#     f.write("============\n")
#     ciudades_region = dictRegiones[region]
#     datos_cansino = total[np.where(ciudades == "Cansino")] / poblacion
#     f.write("Ciudad con mayor porcentaje de inmunizados: " + ciudades[np.argmax(datos_cansino) + "\n"]
#



        
