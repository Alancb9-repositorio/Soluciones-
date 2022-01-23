import numpy as np
dicEspecies = {1:"Lobo de artico", 2:"Oso Polar", 3:"Reno", 4:"Foca", 5:"Pinguino", 6:"Ballena"}
# m = np.array([[1,1,2],
#               [1,2,3],
#               [2,1,4]])
def crearMatriz(nomArchivo):
    f  = open(nomArchivo, "r")
    numero_filas = int(f.readline().strip())
    numero_columnas = int(f.readline().strip())
    matriz_hielo2009 = np.zeros((numero_filas, numero_columnas), dtype = int)
    matriz_hielo2019 = np.zeros((numero_filas, numero_columnas), dtype = int)
    matriz_animales2009 = np.zeros((numero_filas, numero_columnas), dtype = int)
    matriz_animales2019 = np.zeros((numero_filas, numero_columnas), dtype = int)
    f.readline()
    for line in f:
       ano, num_fila, num_columna, hielo, especie = line.strip().split(",")   #["ano", "fila", "columna", "hielo", "especie"]
       if ano == "2009":
           matriz_hielo2009[int(num_fila), int(num_columna)] = int(hielo)
           matriz_animales2009[int(num_fila), int(num_columna)] = int(especie)
       else:
           matriz_hielo2019[int(num_fila), int(num_columna)] = int(hielo)
           matriz_animales2019[int(num_fila), int(num_columna)] = int(especie)
    f.close()
    return matriz_hielo2009, matriz_hielo2019, matriz_animales2009, matriz_animales2019
m1, m2, m3, m4 = crearMatriz("artico2009-2019.txt")
print(m1)
print(m2)
print(m3)
print(m4)
def cuadrantes(matriz):
    filas, columnas = matriz.shape    #(numero_filas, numero_columnas)
    matriz1 = matriz[:filas // 2, :columnas // 2]
    matriz2 = matriz[:filas // 2, columnas // 2:]
    matriz3 = matriz[filas // 2:, :columnas // 2]
    matriz4 = matriz[filas // 2:, columnas // 2:]
    return matriz1, matriz2, matriz3, matriz4
q1, q2, q3, q4 = cuadrantes(m4)
print("-----------------------------------")
print(q1)
print(q2)
print(q3)
print(q4)
print("-----------------------------")
def poblacionEspecie(mAnimales, especie):
    q1, q2, q3, q4 = cuadrantes(mAnimales)
    cant_q1 = np.sum(q1 == especie)
    cant_q2 = np.sum(q2 == especie)
    cant_q3 = np.sum(q3 == especie)
    cant_q4 = np.sum(q4 == especie)
    return  cant_q1, cant_q2, cant_q3, cant_q4
c1, c2, c3, c4 = poblacionEspecie(m4, 1)
print(c1)
print(c2)
print(c3)
print(c4)
print("----------------------------")
def densidadHielo(mHielo):
    q1, q2, q3, q4 = cuadrantes(mHielo)
    densidad_q1 = np.sum(q1) / q1.size
    densidad_q2 = np.sum(q2) / q2.size
    densidad_q3 = np.sum(q3) / q3.size
    densidad_q4 = np.sum(q4) / q4.size
    return densidad_q1, densidad_q2, densidad_q3, densidad_q4
d1, d2, d3, d4 = densidadHielo(m1)
print(d1)
print(d2)
print(d3)
print(d4)
print("----------------------------")
def especieDominante(mAnimales):
    q1, q2, q3, q4 = cuadrantes(mAnimales)
    valores_q1, apariciones_q1 = np.unique(q1[np.where(q1>0)], return_counts = True)
    valores_q2, apariciones_q2 = np.unique(q2[np.where(q2>0)], return_counts = True)
    valores_q3, apariciones_q3 = np.unique(q3[np.where(q3>0)], return_counts = True)
    valores_q4, apariciones_q4 = np.unique(q4[np.where(q4>0)], return_counts = True)
    especie_max_q1 = valores_q1[np.argmax(apariciones_q1)]
    especie_max_q2 = valores_q2[np.argmax(apariciones_q2)]
    especie_max_q3 = valores_q3[np.argmax(apariciones_q3)]
    especie_max_q4 = valores_q4[np.argmax(apariciones_q4)]
    return especie_max_q1, especie_max_q2, especie_max_q3, especie_max_q4
e1, e2, e3, e4 = especieDominante(m4)
print(e1)
print(e2)
print(e3)
print(e4)
print("--------------------------------------")
def migracionEspecie(mAnimales2009, mAnimales2019, especie):
    tupla_2009 = poblacionEspecie(mAnimales2009, especie)
    tupla_2019 = poblacionEspecie(mAnimales2019, especie)
    cuadrantes = np.array(["Q1", "Q2", "Q3", "Q4"])
    cuadrante_maximo_2009 = cuadrantes[np.argmax(np.array(tupla_2009))]
    cuadrante_maximo_2019 = cuadrantes[np.argmax(np.array(tupla_2019))]
    return cuadrante_maximo_2009, cuadrante_maximo_2019
c_max1, c_max2 = migracionEspecie(m3, m4, 3)
print(c_max1)
print(c_max2)
print("--------------------------------------")
def  crearDiccionario(mHielo, mAnimales, dicEspecies):
    d = {}
    densidad_q1, densidad_q2, densidad_q3, densidad_q4 = densidadHielo(mHielo)
    d["densidad hielo"] = {}
    d["densidad hielo"]["Q1"] = densidad_q1
    d["densidad hielo"]["Q2"] = densidad_q2
    d["densidad hielo"]["Q3"] = densidad_q3
    d["densidad hielo"]["Q4"] = densidad_q4
    d["Especies"] = {}
    for clave_especie in dicEspecies.keys():
        tupla_cuadrantes = poblacionEspecie(mAnimales, clave_especie)
        total_poblacion = sum(tupla_cuadrantes)
        d["Especies"][clave_especie] = total_poblacion
    return d
dicc = crearDiccionario(m2, m4, dicEspecies)
print(dicc)