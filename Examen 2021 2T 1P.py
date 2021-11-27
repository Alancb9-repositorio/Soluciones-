#Tema 1 (10 pts)
"""Solucion"""
"""Asuma que este codigo esta completo y no tiene errores de logica o sintaxis.
Para resolver este tema, no utilice ningun editor de python o herramienta de programacion
Que imprime el siguiente codigo?:"""

def filtrar_numeros(numeros, n):
    resultado = []
    for numero in numeros:
        if numero % n != 0:
            resultado.append(numero)
    return resultado

i = 0
for v in filtrar_numeros(range(0, 10), 4):
    print(i, v)
    i = i + 1

#Tema 2 (25 pts)
"""Convierta el siguiente codigo de python que cuenta cuantos elementos hay en la lista
antes del valor cero (0) y lo muestra por pantalla. El objetivo es que utilice un while en lugar del for y poder 
eliminar del codigo el if y la instruccion l_numeros.clear() que forza al for a terminar
cuando se cumple la condicion de que la variable nuymero sea igual a cero, lo cual se considera
una mala practica al programar"""

"""Asuma que la lista l_numeros tiene una longitud variable pero siempre tendra un y solo un cero como
elemento en alguna posicion aleatoria."""

l_numeros = [5, 4, 7, 0, 1]
cont = 0
for numero in l_numeros:
    if numero == 0:
        l_numeros.clear()
    else:
        cont += 1
print(cont)


l_numeros = [5, 4, 7, 0, 1]
cont = 0
while l_numeros[cont] != 0:
    cont += 1
print(cont)

#Tema 3 (30 pts)
"""Implemente la funcion palabras_comunes(lis_frases) que recibe una lista con varias frases como texto.
 Cada frase de la lista esta compuesta de solo palabras separadas por un espacio en blanco entre palabras
 (no hay comas, puntos o ningun otro tipo de simbolos). La funcion retorna una lista con las palabras repetidas
 entre pares adyacentes de una frase. Asegurese de que cada elemento de la lista resultante se incluya UNA sola vez
 en el resultado.
 Ejemplo, dada la lista de frases: frases = ["Al que madruga Dios lo ayuda", "Al pan pan y al vino vino", 
 "Soy espejo y me reflejo", "Programar es lo mas parecido a un superpoder"]
 Palabras repetidas entre "Al que madruga Dios lo ayuda" y "Al pan pan y al vino vino" """

def palabras_comunes(lista_frases):
    palabras_comunes = []
    for indice in range(len(lista_frases) - 1):
        lista_palabras = lista_frases[indice].split()
        frase_adyacente = lista_frases[indice + 1]
        for palabra in lista_palabras:
            if palabra in frase_adyacente:
                palabras_comunes.append(palabra)
    return list(set(palabras_comunes))
frases = ["Al que madruga Dios lo ayuda", "Al pan pan y al vino vino",
 "Soy espejo y me reflejo", "Programar es lo mas parecido a un superpoder"]
print(palabras_comunes(frases))

#Tema 4 (35 pts)
"""Dado el siguiente programa parcial"""
#funciones
def genera_tarifas(Informacion_tarifas):
    Paises_destino = []
    Tarifas_envio_kg = []

    for info in Informacion_tarifas:
        pais, tarifa = info.split("-")
        tarifa = int(tarifa)
        Paises_destino.append(pais)
        Tarifas_envio_kg.append(tarifa)
    return  Paises_destino, Tarifas_envio_kg

#programa principal
catalogo = ["Colombia-5", "EEUU-10", "Peru-7", "Brasil-12"]

"""Comprete el programa principal donde utilice la funcion genera_tarifas para crear las 
listas paralelas con los nombres de los paises y su correspondiente tarifa de envio por kilogramo.

Luego pida al usuario que ingrese un destino por teclado. Usando otro input, pida al usuario que 
ingrese un peso en kilogramos.
Muestre por pantalla el valor a pagar por enviar el paquete con la informacion ingresada.
El usuario podra seguir ingresando datos de paquetes hasta que escriba "terminar" como destino.
Asegurese que su programa no se caiga(genere una exepcion) si el usuario ingresa un pais que no existe en el catalogo.
Finalmente mostrar el total a pagar.

Ejemplo:

Ingrese destino: EEUU
Ingrese peso en Kg: 5.4
[!] El valor a pagar es $54.0
(Comentario para los alumnos, esto equivale a 5.4 x 10
pues el envio a EEUU cuesta $10 por kilogramo segun el
catalogo del ejemplo)

Ingrese destino: Colombia
Ingrese peso en Kg: 7
[!] El valor a pagar es $35.0

Ingrese destino: EEUU
Ingrese peso: 1.28
[!] El valor a pagar es $12.8

Ingrese destino: Peru
Ingrese peso en Kg: 4.3
[!] El valor a pagar es $30.1

Ingrese destino: ya no mas

[!] El total a pagar es $131.9
"""
paises_destino, tarifas_envio = genera_tarifas(catalogo)
destino = input("Ingrese destino: ").strip().lower().capitalize()
peso = input("Ingrese peso en Kg: ")
while not(peso.isdigit()) and (("." not in peso) or (len(peso.split(".")[0]) == 0) or (len(peso.split(".")[1]) == 0) or (peso.split(".")[0].isalpha()) or (peso.split(".")[1].isalpha())):
    print("DATO ERRONEO")
    peso = input("Estimado usuario por favor ingrese nuevamente un peso: ")
total_a_pagar = 0
while destino != "terminar" and destino != "no va mas":
    indice_destino = paises_destino.index(destino)
    valor_a_pagar = tarifas_envio[indice_destino] * peso
    print("[!] El valor a pagar es: {}".format(valor_a_pagar))
    destino = input("Ingrese destino: ").strip().lower().capitalize()
    peso = input("Ingrese peso en Kg: ")
    while not (peso.isdigit()) and (("." not in peso) or (len(peso.split(".")[0]) == 0) or (len(peso.split(".")[1]) == 0) or (peso.split(".")[0].isalpha()) or (peso.split(".")[1].isalpha())):
        print("DATO ERRONEO")
        peso = input("Estimado usuario por favor ingrese nuevamente un peso: ")
    total_a_pagar += valor_a_pagar










