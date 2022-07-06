"""Ejercicio 1 (30 puntos)
Escriba la función swapPrefijo(cadena1,cadena2,num). Esta función recibe :
● Dos cadenas de caracteres
● Un número entero que representa el número de caracteres
La función retorna una cadena de caracteres que sea el resultado de intercambiar los
primeros caracteres de las cadenas (use el parámetro num para la longitud del prefijo). Si la
longitud de alguna de las cadenas es menor al número que recibe la función, la función
retorna un mensaje de error que indica que no se pudo realizar la operación.
En el programa principal, solicite al usuario que introduzca 2 cadenas de caracteres y un
número entero (asuma que es entero) y muestre la cadena generada por la función
swapPrefijo.
Ejemplos de salida:
Ingrese una cadena de caracteres: casita
Ingrese otra cadena de caracteres: ramal
Ingrese un número entero: 3
La cadena resultante es: ramita casal
Ingrese una cadena de caracteres: casita
Ingrese otra cadena de caracteres: ramal
Ingrese un número entero: 8
La cadena resultante es: No se pudo realizar la operación
Ejercicio 2 (25 puntos)
Escriba la función asignaColor(fecha). Esta función recibe :
● Una fecha en formato dd-mm-yyyy (Ej 08-06-2022)
La función retorna una cadena de caracteres con el nombre del mes correspondiente a la
fecha recibida y el color asociado de acuerdo al mes. Por ejemplo:
Mes Junio, color asignado: NEGRO
La función debe hacer uso de 2 listas paralelas:
listaMeses=['Enero','Febrero','Marzo','Abril','Mayo','Junio',
'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembr
e']
listaColores=['ROJO','AZUL','AMARILLO','VERDE','GRIS','NEGRO'
,'BLANCO','ROSADO','VIOLETA','NARANJA','TURQUESA','CAFÉ']
En el programa principal, solicite al usuario una fecha en formato dd-mm-yyyy (asuma que
el usuario va a ingresar la fecha en ese formato) y muestre su nombre de mes y color
correspondiente
Ejemplo de salida:
Ingrese fecha en formato dd-mm-yyyy: 08-06-2022
Mes Junio, color asignado: NEGRO"""

#Ejercicio 1
def swapPrefijo(cadena1,cadena2,num):    #cadena1 = "casita"    cadena2 = "ramal" num = 3
    if (len(cadena1) <  num) or (len(cadena2) <  num):    # (6 < 3) or (5 < 3)   = false or false = false
        return "No se pudo realizar la operacion"
    else:
        p1_cadena1 = cadena1[:num]    #p1_cadena1 = cadena1[:3] = "cas"
        p2_cadena1 = cadena1[num:]    #p2_cadena1 = cadena1[3:] = "ita"
        p1_cadena2 = cadena2[:num]    #p1_cadena2 = cadena2[:3] = "ram"
        p2_cadena2 = cadena2[num:]    #p2_cadena2 = cadena2[3:] = "al"
        nueva_cadena1 = p1_cadena2 + p2_cadena1     #nueva_cadena1 = "ram" + "ita" = "ramita"
        nueva_cadena2 = p1_cadena1 + p2_cadena2    #nueva_cadena2 = "cas" + "al" = "casal"
        return nueva_cadena1 + " " + nueva_cadena2    #"ramita casal"
    
#Programa principal
c1 = input("Ingrese la primera cadena: ")    #c1 = "casita"
c2 = input("Ingrese la segunda cadena: ")    #c2 = "ramal"
numero = int(input("Ingrese un numero: "))    #numero = 3
cadena = swapPrefijo(c1,c2,numero)     #cadena = "ramita casal"
print("La cadena resultante es: {}".format(cadena))

#Ejercicio2
def asignaColor(fecha):
    listaMeses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    listaColores=['ROJO','AZUL','AMARILLO','VERDE','GRIS','NEGRO','BLANCO','ROSADO','VIOLETA','NARANJA','TURQUESA','CAFÉ']
    dia, mes, ano = fecha.split("-") #["dd", "mm", "yyyy"]
    nombre_mes = listaMeses[int(mes) - 1]
    color_mes = listaColores[int(mes) - 1]
    return "Mes " + nombre_mes + ", color asignado: " + color_mes
#Programa principal
fecha = input("Ingrese una fecha: ")
color = asignaColor(fecha)
print(color)

#EJERCICIO 3
#Funcion
def  fechaValida(cadena):
    return cadena[:2].isdigit() and cadena[2] == "/" and cadena[3:5].isdigit() and cadena[5] == "/" and cadena[6:10].isdigit()
#programa principal
fecha = input("Ingrese fecha: ")
if fechaValida(fecha):
    print("La fecha SI cumple con el formato")
else:
    print("La fecha NO cumple con el formato")


#EJERCICIO 4
#Funcion
def valorMayor(cadena1):
    return max(cadena1.strip().split())
#Programa principal
registro = "81 20 45 67 40 33 34 45 60 50 70 80 "
temperatura_max = valorMayor(registro)
print("El valor de temperatura mayor es de: {}".format(temperatura_max))
temperatura = int(input("Ingrese una temperatura: "))
if temperatura > int(temperatura_max):
    print("El valor {} es Mayor a la temperatura maxima registrada".format(temperatura))
elif temperatura == int(temperatura_max):
    print("El valor {} es Igual a la temperatura maxima registrada".format(temperatura))
else:
    print("El valor {} es Menor a la temperatura maxima registrada".format(temperatura))


#EJERCICIO 4
#Funcion
def valorMayor(cadena1):
    numero_max = 0
    for numero in cadena1.strip().split():
        if int(numero) > numero_max:
            numero_max = int(numero)
    return numero_max
#Programa principal
registro = "81 20 45 67 40 33 34 45 60 50 70 80 "
temperatura_max = valorMayor(registro)
print("El valor de temperatura mayor es de: {}".format(temperatura_max))
temperatura = int(input("Ingrese una temperatura: "))
if temperatura > temperatura_max:
    print("El valor {} es Mayor a la temperatura maxima registrada".format(temperatura))
elif temperatura == temperatura_max:
    print("El valor {} es Igual a la temperatura maxima registrada".format(temperatura))
else:
    print("El valor {} es Menor a la temperatura maxima registrada".format(temperatura))