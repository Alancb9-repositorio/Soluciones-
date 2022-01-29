import numpy as np
dic_peliculas_ciudades = {
    "Madrid": ["Rapido y Furioso 9", "Despicable me"],
    "Estambul": ["Jurassic Park", "Encanto"],
    "Quito": ["Encanto", "Extincion", "Spiderman"],
    "Moscu": ["Extincion", "Rapido y Furioso 9"],
    "Turquia": ["Iron Man"],
    "Chicago": ["Encanto", "Jurassic Park"]
}
dic_movies = {
    "Rapido y Furioso 9": ["Paul Walker", "Vin diesel", "Dwayne Johnson", "Universal"],
    "Despicable me": ["Gwyneth Paltrow", "Bruce Willis", "Universal"],
    "Encanto": ["Stephanie Beatriz", "Jessica Darrow", "Diane Guerrero", "Disney"],
    "Spiderman": ["Tom Holland", "Sony"]
}
#TEMA 1
def crearMatrizDta(dic_peliculas_ciudades):
    vector_ciudades = np.array(list(dic_peliculas_ciudades.keys()))
    vector_peliculas = []
    for lista_peliculas in dic_peliculas_ciudades.values():
        vector_peliculas += lista_peliculas
    vector_peliculas = np.array(list(set(vector_peliculas)))
    matriz = np.random.randint(4, 18, (vector_ciudades.size, vector_peliculas.size))
    return vector_ciudades, vector_peliculas, matriz
#TEMA 2
def obtenerTop_n(matriz, v_names_filas, v_names_cols, dic_movies, n, estudio):
    top_n_peliculas = []
    top_n_valores = []
    vector_total_semanas = np.sum(matriz, axis = 0)             #RESUELTO POR EL BICHO
    for pelicula, lista_info in dic_movies.items():
        if lista_info[-1] == estudio:
            top_n_peliculas.append(pelicula)
            top_n_valores.append(vector_total_semanas[np.sum(np.where(v_names_cols == pelicula))])
    return np.array(top_n_peliculas)[np.argsort(np.array(top_n_valores))[::-1][:n]]
#TEMA 3
#Literal 1
ciudades, peliculas, matriz = crearMatrizDta(dic_peliculas_ciudades)
promedio_semanas_cartelera = mp.mean(matriz, axis = 0)
for indice in range(promedio_semanas_cartelera.size):
    print("La pelicula {} tuvo un promedio de {} semanas en cartelera.".format(peliculas[indice], promedio_semanas_cartelera[indice]))
#Literal 2
vector_turquia = matriz[np.sum(np.where(ciudades == "Turquia")), :]
vector_madrid = matriz[np.sum(np.where(ciudades == "Madrid")), :]
turquia_menor_madrid = peliculas[vector_turquia < vector_madrid]
print("La peliculas que tuvieron menos semanas en cartelera en turquia que en madrid son:")
for pelicula in turquia_menor_madrid:
    print(pelicula)
#Literal 3
vector_quito = matriz[np.sum(np.where(ciudades == "Quito")), :]             #RESUELTO POR EL BICHO
peli_max_quito = peliculas[np.argmax(vector_quito)]
estudio = dic_movies[peli_max_quito][-1]
print("El nombre de la pelicula que mas semanas en cartelera tuvo en Quito es {} que pertenece al estudio llamado {}".format(peli_max_quito, estudio))
#Literal 4
vector_top_4 = obtenerTop_n(matriz, ciudades, peliculas, dic_movies, 4, "Universal")
print("Las 4 peliculas con mas semanas en cartelera del estudio Universal son:")
for pelicula in vector_top_4:
    print(vector_top_4)
#Literal 5
vector_moscu = matriz[np.sum(np.where(ciudades == "Moscu")), :]
promedio_moscu = np.mean(vector_moscu)
mas_que_promedio = peliculas[vector_moscu > promedio_moscu]
print("Las peliculas que tuvieron mas semanas en cartelera en Moscu que el promedio son:")
for pelicula in mas_que_promedio:
    print(pelicula)
#TEMA 4
f = open("carteleraQuito.csv", "w")
f.write("Pelicula|semanas en cartelera|estudio\n")      #EL BICHO ES ETERNO
for indice in range(vector_quito.size):
    f.write(peliculas[indice] + "|" + str(vector_quito[indice]) + "|" dic_movies[peliculas[indice]][-1] + "\n")
f.close()


        
        