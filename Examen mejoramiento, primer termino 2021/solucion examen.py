#SOLUCION
#Tema1
def leer_info(name_file):
    f = open(name_file)
    etiqueta_vacante, total_vacante = f.readline().strip().split(":") #["Total plazas vacantes", " 1870"]
    total_vacante = int(total_vacante.strip())
    f.readline()
    d = {}
    for line in f:
        ciudad, empresa, cod_vacante, cargo, sueldo, horas_extras, horario, habilidades= line.strip().split(",")   #["Ciudad" ,"Empresa" , "Codig_plaza_vacante" ,"Cargo", "Sueldo", "Horas_extras", "Horario", "Habilidades"]
        d[ciudad] = d.get(ciudad, {})
        d_info = {}
        d_info["Codigo_plaza_vacante"] = int(cod_vacante)
        d_info["Cargo"] = cargo
        d_info["Sueldo"] = int(sueldo)
        if horas_extras == "Si":
            d_info["Horas_Extras"] = True
        else:
            d_info["Horas_Extras"] = False
        d_info["Horario"] = horario
        d_info["Habilidades"] = set(habilidades.split("|"))
        d[ciudad][empresa] = d[ciudad].get(empresa, []) + [d_info]
    f.close()
    return d, total_vacante

#Tema2
def buscar_codvacantes(texto, dic_vacantes):
    l = []
    for dicc_empresa in dic_vacantes.values():
        for lista_info in dicc_empresa.values():
            for dicc_caracteristicas in lista_info:
                if dicc_caracteristicas["Cargo"] == texto or (texto in dicc_caracteristicas["Habilidades"]):
                    l.append(dicc_caracteristicas["Codigo_plaza_vacante"])
    return l

#Tema3
#a
import numpy as np
m = np.array([[1,2],
             [3,4],
             [5,6],
             [7,8],
             [9,10]])
print(m[-3:, :])        
matrix_sueldos = np.array([1,2,3,4,5])  #Es para que no arroje error siuuu
matrix_vacantes = np.array([1,2,3,4,5]) #Es para que no arroje error siuuu
l_etiquetas_filas = ["Quito", "Cuenca"] #Es para que no arroje error siuuu
l_etiquetas_columnas = ["Aux.Limpieza", "Albanil"]  #Es para que no arroje error siuuu
f = open("informacion.txt", "w")
indice_secretaria = l_etiquetas_columnas.index("Secretaria")
recorte_secretaria = matrix_sueldos[:, indice_secretaria]
top_6 = np.argsort(recorte_secretaria)[::-1][:6]
cont = 1
for indice in top_6:
    f.write(str(cont) + ". " + l_etiquetas_filas[indice] + ",$" + str(recorte_secretaria[indice]) + "\n")
    cont += 1

#b
dic_vacantes = {}   #Es para que no arroje error siuuu
lista_codigos = buscar_codvacantes("Condicion fisica", dic_vacantes)
f.write(", ".join(lista_codigos) + "\n")

#c
sum_filas = np.sum(matrix_vacantes, axis=1)
ciudad_mas_vacantes = l_etiquetas_filas[np.argmax(sum_filas)]
f.write(ciudad_mas_vacantes + "\n")

#d
indice_albanil = l_etiquetas_columnas.index("Albanil")
recorte_albanil =  matrix_sueldos[:, indice_albanil]
promedio = np.mean(recorte_albanil)
f.write("$" + str(promedio) + "\n")

#e
indice_quevedo = l_etiquetas_filas.index("Quevedo")
recorte_quevedo = matrix_sueldos[indice_quevedo, :]
ciudades_respuesta = np.array(l_etiquetas_columnas)[recorte_quevedo > 380]
f.write(", ".join(list(ciudades_respuesta)) + "\n")

#f
indice_bombero = l_etiquetas_columnas.index("Bombero")
suma_de_sueldos = recorte_secretaria + matrix_sueldos[:, indice_bombero]
for indice in range(len(suma_de_sueldos)):
    f.write(l_etiquetas_filas[indice] + ":$" + str(suma_de_sueldos[indice]) + "\n")
f.close()


#Tema4
indice_enfermeria = l_etiquetas_columnas.index("Enfermeria")
recorte_ciudades_oriente_sueldos = matrix_sueldos[-8:, indice_enfermeria]
recorte_ciudades_oriente_vacantes = matrix_vacantes[-8:, indice_enfermeria]
ciudades_oriente = l_etiquetas_filas[-8:]
indice_maximo = np.argmax(recorte_ciudades_oriente_vacantes[recorte_ciudades_oriente_sueldos >= 414.23])
print(ciudades_oriente[indice_maximo])