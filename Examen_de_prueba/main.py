import numpy as np
M = np.array([[20, 30, 19, 15, 18],
              [89,195,120,150,240],
              [65,165,100,110,200],
              [30, 49, 35, 89, 67],
              [ 5, 1.8,  1,  2,  5]])
huracanes = {2016:('Alex', 'Otto'),
             2017:('Ariene', 'Harvey','Irma')
             }
#Tema1
def  total_marejada(M, cat):
    vector_velocidad_viento = M[2, :]
    vector_marejada = M[-1, :]
    if cat == 1:
        total_marejada = np.sum(vector_marejada[vector_velocidad_viento < 100])
    elif cat == 2:
        total_marejada = np.sum(vector_marejada[vector_velocidad_viento >= 100 & vector_velocidad_viento < 150])
        #total_marejada = np.sum(vector_marejada[100 >= vector_velocidad_viento < 150])
    elif cat == 3:
        total_marejada = np.sum(vector_marejada[vector_velocidad_viento >= 150 & vector_velocidad_viento < 200])
    elif cat == 4:
        total_marejada = np.sum(vector_marejada[vector_velocidad_viento >= 200 & vector_velocidad_viento <= 250])
    else:
        total_marejada = np.sum(vector_marejada[vector_velocidad_viento > 250])
    return total_marejada
marejada = total_marejada(M, 1)
print(marejada)

#literal 2
def indices_ano(huracanes, ano):
    cont = 0
    ind_inicial = 0
    ind_final = 0
    for ano1, tupla_huracanes in huracanes.items():
        if ano1 != ano:
            cont += len(tupla_huracanes)
        else:
            ind_inicial = cont
            ind_final = cont + len(tupla_huracanes)
    return ind_inicial, ind_final - 1
print(indices_ano(huracanes, 2017))

#literal 3
def velocidad_superior(M, huracanes, ano):
    indice_inicial, indice_final = indices_ano(huracanes, ano)
    vector_velocidad_desplazamiento = M[0, ind_inicial:indice_final + 1]
    promedio = np.mean(vector_velocidad_desplazamiento)
    respuesta = vector_velocidad_desplazamiento > promedio
    return np.sum(respuesta)

#Literal 4
def ACE(M, huracanes, ano):
    indice_inicial, indice_final = indices_ano(huracanes, ano)
    vector_velocidad_viento = M[2, ind_inicial:indice_final + 1]
    cantidad_energia = np.sum(vector_velocidad_viento ** 2) * (10 ** -4)
    return cantidad_energia

#Literal 5
def lluvia(M, huracanes, nombre_huracan, ano):
    indice_inicial, indice_final = indices_ano(huracanes, ano)
    vector_lluvia = M[3, ind_inicial:indice_final + 1]
    indice_huracan = huracanes[ano].index(nombre_huracan)
    return vector_lluvia[indice_huracan]
#Tema 2
#Literal a
def cargarDatos(narchivo):
    l = []
    d = {}
    f = open(narchivo, "r")
    f.readline()
    for line in f:
        id_ruta, id_chofer, fecha = line.strip().split(",")
        d[fecha] = d.get(fecha, {})
        d[fecha][id_ruta] = d[fecha].get(id_ruta, []) + [id_chofer]
        l.append(id_chofer)
    f.close()
    return set(l), d

#Literal B
def encontrarChoferes(datos, loschoferes, unafecha, unaruta, n):
  conj=set()
  for i in range(n+1):
    dia, mes, anio =unafecha.split('-')
    dianuevo = int(dia)-i
    fechanueva=str(dianuevo)+'-'+ mes+'-'+anio
    lista_conduc= datos[fechanueva][unaruta]
    for elemento in lista_conduc:
      conj.add(elemento)
  inter = loschoferes - conj
  return inter

#Literal C
def grabarArchivo(datos, loschoferes, unafecha, unaruta, n):
    conjunto_choferes = encontrarChoferes(datos, loschoferes, unafecha, unaruta, n)
    f = open(unaruta + "_" + unafecha + .txt, "w")
    f.write("Para la ruta " + unaruta + " los choferes disponibles para la fecha " + unafecha + " que no hayan manejado " + n + " dias anteriores son:\n")
    for chofer in conjunto_choferes:
        f.write(chofer + "\n")
    f.close()

#Literal d
for fecha in datos.keys():
    fecha_n_anterior = calcular_fecha(fecha, 2)
    dicc_rutas = datos[fecha_n_anterior]
    for ruta, lista_choferes in dicc_rutas.items():
        f = open(ruta + "_" + fecha + .txt, "w")
        f.write("Para la ruta " + ruta + " los choferes disponibles para la fecha " + fecha + " que no hayan manejado " + 2 + " dias anteriores son:\n")
        for chofer in lista_choferes:
            f.write(chofer + "\n")
        f.close()

#Tema 3
#Literal 1
# = 2   #x = 2
y = 5   #y = 5
z = x + z   #z = x + z
print("La suma es ,z")

#Literal 2
A = [3, 2, 7, 5]   
B = [31, 5, 4, 8, 12, 3, -9, 6]     
C = 0 
N = 3 
for i in range(0, 4) :
    B[A[i]] = B[A[i]] + N 
    C += B[A[i]] 
print(C)

# A = [3, 2, 7, 5]
# B = [31, 5, 7, 11, 12, 6, -9, 7]
# C = 33
# N = 3 
# range = (0,1,2,3)
#iteracion 1
#i = 0
#B[3] = 11 
#C += 11 
#iteracion 2
#i = 1
#B[2] = 7
#C += 7
#iteracion 3
#i = 2
#B[7] = 9
#C += 9
#iteracion 3
#i = 3
#B[5] = 6
#C += 6
#print(C) >>> 33

#Literal 3
import numpy as np

L = [10,12,11,4,8]
M = [4,2,1,2,7]
matriz = np.array([],int)
A = np.append(matriz,L[2:4])
B = np.append(A,M[1:3]).reshape((2,2))
C = (A * B)//2
print(C)

#import numpy as np
#L = [10,12,11,4,8]
#M = [4,2,1,2,7]
#matriz = ([])
#A = ([11, 4])
#B = ([11, 4, 2, 1]).reshape((2,2)) = ([[11, 4],
#                                       [2, 1]])
#C = (([11, 4]) * ([[11, 4], // 2
#                   [2, 1]]))
