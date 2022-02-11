""" REFERENCIA PRIMERA EVALUACIÓN - II TÉRMINO 2016-2017/ Diciembre 6, 2016
Nuestros robots siempre están trabajando para mejorar sus habilidades lingüísticas. Para esta misión, investigan el 
alfabeto latino y sus aplicaciones.
Vocales - A E I O U
Consonantes - B C D F G H J K L M N P Q R S T V W X Y Z
Suponga que se le da un bloque de texto con diferentes palabras. Estas palabras están separadas por un espacio en 
blanco o un punto. No habrán dos o más espacios en blanco seguidos o combinaciones de espacios en blanco y 
puntos. No habrán vocales con tildes en el texto. Pueden haber números en el texto pero no se consideran palabras 
en esta misión (una mezcla de letras y dígitos no es una palabra tampoco).
Usted debe contar el número de palabras que tienen la misma cantidad de vocales y consonantes. Las mayúsculas y 
minúsculas no son significativas para esta misión.
Desarrolle un programa en Python que pida un bloque de texto por teclado y muestre por pantalla la cantidad de 
palabras que cumplen con la descripción anterior. Por ejemplo:"""
vocales = "AEIOU"
consonantes = "BCDFGHJKLMNPQRSTVWXYZ"
frase = input("Ingrese una frase: ").upper() #"h0la muneco" "hola.muneco"
if "." in frase:
    lista_de_palabras = frase.split(".")    #["hola", "muneco"]
elif " " in frase:
    lista_de_palabras = frase.split(" ")    #["hola", "muneco"]
contador_palabras = 0
for palabra in lista_de_palabras:
    if palabra.isalpha():
        contador_consonante = 0
        contador_vocales = 0
        for letra in palabra:
            if letra in vocales:
                contador_vocales += 1
            elif letra in consonantes:
                contador_consonante += 1
        if contador_consonante == contador_vocales:
            contador_palabras += 1
print(contador_palabras)

def cuenta_palabra(frase):
    frase = frase.upper()
    vocales = "AEIOU"
    consonantes = "BCDFGHJKLMNPQRSTVWXYZ"
    if "." in frase:
        lista_de_palabras = frase.split(".")    #["hola", "muneco"]
    elif " " in frase:
        lista_de_palabras = frase.split(" ")    #["hola", "muneco"]
    contador_palabras = 0
    for palabra in lista_de_palabras:
        if palabra.isalpha():
            contador_consonante = 0
            contador_vocales = 0
            for letra in palabra:
                if letra in vocales:
                    contador_vocales += 1
                elif letra in consonantes:
                    contador_consonante += 1
            if contador_consonante == contador_vocales:
                contador_palabras += 1
    return contador_palabras

resultado = cuenta_palabra("hola mundo")
print(resultado)
