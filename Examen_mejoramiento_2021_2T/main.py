import numpy as np 
#Tema1
def dineniarMatriz(file):
    codigos = []
    f = open(file)
    for line in f:
        num_semana, cod_producto, nombre_producto, unidades_vendidas = line.strip().split(",")
        if cod_producto not in codigos:
            codigos.append(cod_producto)
    f.close()
    matriz = np.zeros((len(codigos), 52), dtype = int)  #resuelto por el bicho siuuuu
    f = open(file)
    for line in f:
        num_semana, cod_producto, nombre_producto, unidades_vendidas = line.strip().split(",")
        matriz[codigos.index(cod_producto), int(num_semana)] = int(unidades_vendidas)
    f.close()
    return np.array(codigos),matriz

#Tema2
def calcular_prom(M, v_nombres_filas, codigo):  #resuelto por el bicho siuuuu
    return np.mean(M[np.sum(np.where(v_nombres_filas == codigo)), :])

#Tema3
#Literal 1  
vector_codigos, matriz = dineniarMatriz("ventas2020.csv")   #resuelto por el bicho siuuuu

#Literal 2
venta_anual = np.sum(matriz, axis=1)
ventas_ordenadas = np.argsort(venta_anual)[:3]
print("Los 3 productos que menos unidades vendidas tuvieron son: ")
for indice in ventas_ordenadas:             #resuelto por el bicho siuuuu
    print("{} con {} unidades vendidas.".format(vector_codigos[indice], venta_anual[indice]))

#Literal 3
promedio_codigo = calcular_prom(matriz, vector_codigos, "COD_12350")
recorte = matriz[np.sum(np.where(vector_codigos == "COD_12350")), :]
total_semanas = np.sum(np.where(recorte > promedio_codigo)) #resuelto por el bicho siuuuu
print("El numero de semanas es: {}".format(total_semanas))

#Literal 4
primer_semestre = matriz[:, :26]
segundo_semestre = matriz[:, 26:]
suma_primer_semestre = np.sum(primer_semestre, axis = 1)
suma_segundo_semestre = np.sum(segundo_semestre, axis = 1)
resultado = vector_codigos[segundo_semestre > primer_semestre]
print("Los prodcutos son: ")
for codigo in resultado:    #resuelto por el bicho siuuuu
    print(codigo)

#Tema 4
dicInventario = {"COD_12350":4, "COD_22119":8, "COD_34745":34}
f1 = open("Cantidadesfaltantes.csv", "w")
f1.write("Semana (1-52);cod_producto;nombre_producto;unidades_faltantes\n")
f1.close()
f2 = open("ventas2021.csv")
for line in f2:
    num_semana, cod_producto, nombre_producto, unidades_vendidas = line.strip().split(",")
    valor_inventario = dicInventario[cod_producto]
    nuevo_valor = valor_inventario - int(unidades_vendidas)
    if nuevo_valor > 0:
        dicInventario[cod_producto] = nuevo_valor
    else:       #resuelto por el bicho siuuuu
        valor_matriz = M[np.sum(np.where(vector_codigos == cod_producto)), int(num_semana) - 1]
         dicInventario[cod_producto] = valor_matriz
        f1 = open("Cantidadesfaltantes.csv", "a")
        f1.write(num_semana + ";" + cod_producto + ";" + nombre_producto + ";" + str(nuevo_valor * (- 1)) + "\n")
        f1.close()
f2.close()

