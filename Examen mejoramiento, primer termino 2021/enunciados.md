TEMA1 (100 PUNTOS)
Usted esta disenando una aplicacion para unir a trabajador con empleos. Para esto, los empleadores agregan la informacion de las plazas de las vacantes en un archivo empleo_disponible.csv con un formato similar al del ejemplo a continuacion:

Total plazas vacantes: 1870
Ciudad,Empresa,Codig_plaza_vacante,Cargo,Sueldo,Horas_extras,Horario,Habilidades
Quito,Rubiasa S.A.,500236,Aux. Limpieza,520,Si,9-17,Normas de limpieza|Condicion fisica...
Cuenca,Etinec S.A.,364189,Albanil,408,No,8-16,Lectura planos|...
Quito,Rubiasa S.A,471421,Secretaria,670,No,8-17,Oficinista|Gestion|...
....
Naranjal,...
...

Entonces, implemente las siguientes funciones:
1.[30 PUNTOS] la funcion leer_info(name_file) que recibe el nombre del archivo con vacantes. La funcion retorna una tupla donde el primer elemento es un diccionario de vacantes y el segundo elementos es el numero total de vacantes. El diccionario debe tener la siguiente estructura:
Ejemplo del diccionario de la tupla a retornar:

{"Quito": {"Rubiasa S.A.": [{"Codigo_plaza_vacante": 500236,
                            "Cargo": "Aux. Limpieza",
                            "Sueldo": 520,
                            "Horas_Extras": True,
                            "Horario": "9-17",
                            "Habilidades": {"Normasde limpieza", "Condicion fisica",....}
                            },
                            {"Codigo_plaza_vacante": 471421,
                            "Cargo": "Secretaria",
                            "Sueldo": 670,
                            "Horas_Extras": False,
                            "Horario": "8-17",
                            "Habilidades": {"Ofimatica", "Gestion",....}

                            },...
                            ],
            }
 "Cuenca": {"Etinec S.A.": [{"Codigo_plaza_vacante": 364189,
                            "Cargo": "Albanil",
                            "Sueldo": 408,
                            "Horas_Extras": False,
                            "Horario": "8-16",
                            "Habilidades": {"Trabajo en equipo", "Condicion fisica",....}
                            },....
                            ],
                            .....

 },
 ......      
}
2.[15 PUNTOS] buscar_codvacantes(texto, dic_vacantes) que recibe un texto a buscar y el diccionario de vacantes. La funcion retorna una lista con todos los codigos de las vacantes cuyos puestos o habilidades coincidan con el texto a buscar. Si al menos uno de ellos(puesto o habilidad) coincide, se considera la vacantes para ser incluida en la lista.
Por ejemplo,

buscar_codvacantes("Aux. limpieza", dic_vacantes) retorna [500236]
buscar_codvacantes("Aux.", dic_vacantes) retorna []
buscar_codvacantes("Condicion fisica", dic_vacantes) retorna [500236, 364189]

Para el resto del examen:
Asuma que tiene la siguiente matriz de Numpy matrix_sueldos, donde las filas representan ciudades del pais, las columnas representan puestos de trabajo y las celdas representan el sueldo promedio mensual en dolares para cada puesto de trabajo en cada ciudad. ejemplo:


Tambien se tiene la matriz matrix_vacantes de iguales dimensiones que la matriz anterior donde las filas representan ciudades del pais, las columnas representan puestos de trabajo y las celdas representan el numero de vacantes para cada puesto de trabajo en cada ciudad. Ejemplo:


Finalmente asuma que tiene las siguientes dos listas:
l_etiquetas_filas = ["Quito",...."Cuenca"]
l_etiquetas_columnas = ["Aux.Limpieza",..."Albanil"]

3.[45 PUNTOS] Analice sus datos y genere un archivo txt con la siguiente informacion:
informacion
***********

a)Las 6 ciudades del pais que mejor sueldo promedio tienen para Secretaria, ordenados descendentemente por sueldo:
1. Quito,$553.17
2. Naranjal,$300.12
3. Quevedo,$295.17
5. Esmeraldas,$215.32
6. Protoviejo,$207.85

b) Codigos de vacantes disponibles para "Condicion Fisica"
500236, 364189

c) Ciudad con mas vacantes de trabajo disponibles en total:
Esmeraldas

d)El sueldo promedio para albanil considerendo todas las ciudades:
$487.38

e)Todos los puestos de trabajo que pagan mas de $380 en Quevedo
Enfermeria, Secretaria

f) Sueldo que se ganaria en cada ciudad trabajando al mismo como secretaria y bombero
Quito:$725.87
....
Cuenca:$1053.12

4.[10 PUNTOS] Asuma que las ultimas 8 filas representan ciudades del oriente ecuatoriano. Muestra por pantalla el nombre de la ciudad del oriente que mas vacantes tiene para enfermeria con un sueldo mayor o igual a $414.23

