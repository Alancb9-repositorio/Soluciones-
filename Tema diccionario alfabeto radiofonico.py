"""El alfabeto radiofónico establecido por Organización de Aviación Civil Internacional (OACI),
es un lenguaje para la comunicación empleado cuando es importante que no se produzcan errores en la comprensión de datos o códigos,
tal como para deletrear la identificación de un contenedor de carga, una aeronave, etc.

a) Realice una función coderadio(dic,secuencia) que reciba una secuencia de letras
y el diccionario radiofonico, y entregue una cadena de caracteres con las palabras del alfabeto radiofónico. Ejemplo:
 
>>coderadio(radiofonico, ‘ESPOL’)
 ans= Echo Sierra Papa Oscar Lima
 
b) Escriba una función decoradio(dic,cadena) que reciba el diccionario radiofonico y 
una cadena de caracteres con las palabras del alfabeto radiofónico,
y muestre la secuencia de letras. Ejemplo:

>>decoradio(radiofonico,‘Echo Sierra Papa Oscar Lima’)
 ans=ESPOL
"""
radiofonico = {'A':'Alfa', 'B':'Bravo', 'C':'Charlie',
               'D':'Delta', 'E':'Echo', 'F':'Foxtrot',
               'G':'Golf', 'H':'Hotel', 'I':'India',
               'J':'Juliet', 'K':'Kilo', 'L':'Lima',
               'M':'Mike', 'N':'November','O':'Oscar',
               'P':'Papa', 'Q':'Quebec','R':'Romeo',
               'S':'Sierra', 'T':'Tango', 'U':'Uniform',
               'V':'Victor', 'W':'Whiskey','X':'X-ray',
               'Y':'Yankee', 'Z':'Zulu'}

#literal a
def coderadio(dic, secuencia): #secuencia = "ESPOL"
    traduccion = "" #traduccion =  "Echo Sierra Papa Oscar Lima"
    for letra in secuencia: #1 letra = "E" 2 letra = "S" 3 letra = "P"  4 letra = "O" 5 lestra = "L"
        significado = dic[letra]    #significado = dic["L"] = "Lima"
        traduccion += " " + significado #traduccion += " " + "Lima"
    return traduccion.strip() #"Echo Sierra Papa Oscar Lima"

#literal b
def decoradio(dic, cadena):
    d = {}
    for clave, valor in dic.items():
        d[valor] = clave
    traduccion = ""
    lista = cadena.split(" ")
    for palabra in lista:
        significado = d[palabra]
        traduccion += significado
    return traduccion


resultado = coderadio(radiofonico, "ESPOL")
print(resultado)

resultado2 = decoradio(radiofonico, "Echo Sierra Papa Oscar Lima")
print(resultado2)

