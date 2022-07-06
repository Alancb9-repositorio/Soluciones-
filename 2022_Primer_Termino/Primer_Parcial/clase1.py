#para comentar o descomentar ctrl + /
# mensaje = "#SISMO ID: igepn2016uzom Rev. 2016/10/25-09:26:09 TL Mag:3.5 Prof 16.48 km, 26.58km Velasco Ibarra,Guayas."
# parte1, parte2 = mensaje.split("TL")    #["#SISMO ID: igepn2016uzom Rev. 2016/10/25-09:26:09 ", " Mag:3.5 Prof 16.48 km, 26.58km Velasco Ibarra,Guayas."]
# datos1, datos2, datos3 = parte2.split(",")    #[" Mag:3.5 Prof 16.48 km", " 26.58km Velasco Ibarra", "Guayas."]
# distancia, ciudad = datos2.split("km")    #[" 26.58", " Velasco Ibarra"]
# magnitud, profundidad = datos1.split("Prof")    #[" Mag:3.5 ", " 16.48 km"]
# letra_magnitud, cantidad_magnitud = magnitud.split(":")    #[" Mag", "3.5 "]
# profundidad = profundidad.replace(" km", "") #" 16.48"
# print("Se ha registrado un sismo a una distancia de{} KM de la ciudad de{} perteneciente a la provincia del {} con una magnitud de {}Km en la escala de Richter y una profundidad de{} Km".format(distancia, ciudad.upper(), datos3.replace(".", "").upper(), cantidad_magnitud, profundidad))

# numero = input("Ingrese un numero telefonico: ")    #"0968312979"
# if numero.startswith("09") or numero.startswith("08"):
#     print("Empieza con 09 o 08?: True")
# else:
#     print("Empieza con 09 o 08?: False")
# if numero[:2] == "09" or numero[:2] == "08":
#     print("Empieza con 09 o 08?: True")
# else:
#     print("Empieza con 09 o 08?: False")
# print("Empieza con 09 o 08?: {}".format(numero.startswith("09") or numero.startswith("08")))
# print("Empieza con 09 o 08?: {}".format(numero[:2] == "09" or numero[:2] == "08"))
# print("Tiene 11 caracteres?: {}".format(len(numero) == 11))

# puntuacion = float(input("Ingrese la puntuacion: "))
# if puntuacion == 0.0:
#     print("Su rendimiento es inaceptable")
#     print("Su cantidad de dinero es: 0")
# elif puntuacion == 0.4:
#     print("Su rendimiento es aceptable")
#     print("Su cantidad de dinero es: {}".format(2400 * 0.4))
# elif puntuacion >= 0.6:
#     print("Su rendimiento es meritorio")
#     print("Su cantidad de dinero es: {}".format(2400 * 0.6))
# else:
#     print("Este valor no es aceptado")
# pregunta = input("Desea un pizza vegetariana? ").lower()
# if pregunta == "si":
#     print("Ingredientes disponibles\n"
#           "Pimiento\n"
#           "Peperoni\n"
#           "Tofu\n"
#           "Jamon\n"
#           "Salmon")
#     ingrediente = input("Escoja un ingrediente: ").lower()
#     vegetariana = ["pimiento", "tofu"]
#     no_vegetariana = ["peperoni", "jamon", "salmon"]
#     if ingrediente in vegetariana:
#         print("la pizza elegida es vegetariana")
#         print("Su pizza contiene",ingrediente,"-","mozzarella-tomate")
#     elif ingrediente in no_vegetariana:
#         print("La pizza elegida es no vegetariana")
#         print("Su pizza contiene",ingrediente,"-","mozzarella-tomate")
#     else:
#         print("El ingresdiente ingresado no esta disponible")
# elif pregunta == "no":
#     print("Ingredientes disponibles\n"
#           "Pimiento\n"
#           "Peperoni\n"
#           "Tofu\n"
#           "Jamon\n"
#           "Salmon")
#     ingrediente = input("Escoja un ingrediente: ").lower()
#     vegetariana = ["pimiento", "tofu"]
#     no_vegetariana = ["peperoni", "jamon", "salmon"]
#     if ingrediente in vegetariana:
#         print("la pizza elegida es vegetariana")
#         print("Su pizza contiene",ingrediente,"-","mozarella-tomate")
#     elif ingrediente in no_vegetariana:
#         print("La pizza elegida es no vegetariana")
#         print("Su pizza contiene",ingrediente,"-","mozzarella-tomate")
#     else:
#         print("El ingresdiente ingresado no esta disponible")
# fecha = input("Ingrese la fecha en formato dd-nd-mm: ")    #"dd-nd-mm"
# dia, numero_dia, numero_mes = fecha.split("-")    #["dd", "nd", "mm"]
# if int(dia) < 1 or int(dia) > 5:   
#     print("Fin del programa, ocurrio un ERROR")
# elif int(numero_dia) <1 or int(numero_dia) > 31:
#     print("Fin del programa, ocurrio un ERROR")
# elif int(numero_mes) <1 or int(numero_mes) > 12:
#     print("Fin del programa, ocurrio un ERROR")
# else:
#     if int(dia) == 1 or int(dia) == 2 or int(dia) == 3:
#         examen = input("Ese dia se tomaron examenes? ").lower()
#         if examen == "si":
#             aprobados = int(input("Ingrese la cantidad de aprobados: "))
#             reprobados = int(input("Ingrese la cantidad de reprobados: "))
#             suma = aprobados + reprobados
#             porcentaje_reprobados = (reprobados * 100) / suma
#             print("El procentaje de reprobados es: {}".format(porcentaje_reprobados))
#     elif int(dia) == 4:
#         asistencia = int(input("Ingrese el porcentaje de asistencia"))   #50
#         if asistencia >= 50:
#             print("Asistio la mayoria")
#         else:
#             print("No asistio la mayoria")
#     elif int(dia) == 5 and (numero_dia == 1) and (numero_mes == 1 or numero_mes == 7):
#         print("Comienzo de nuevo ciclo")
#         cantidad_alumnos = input("Ingrese la cantidad de4 alumnos del nuevo ciclo: ")
#         arancel = input("Ingrese el arancel por cada alumno: ")
#         total = cantidad_alumnos * arancel
#         print("El ingreso total es: {}".format(total))