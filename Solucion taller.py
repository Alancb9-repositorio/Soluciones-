"""Muestre el nombre y la edad desde el mas joven hasta el menos joven"""
names = {"timothy": 17,"jane":12,"john":21,"peter":25}
lista_nombres = list(names.keys())  #lista_nombres = ["timothy", "jane", "john", "peter"]
lista_nombres.sort() #["jane", "john", "peter", "timothy"]
for datos in range(len(lista_nombres)): #(0,1,2,3) 1ra datos = 0 2da datos = 1 3ra datos = 2 4ta datos = 3
    nombre = lista_nombres[datos]  #pos_nombres = lista_nombres[3] = "timothy"
    edad=  names[nombre]    #pos_edades = name["john"] = 17
    print(nombre,edad) #jane 12
                             #jhon 12
                             #peter 25
                             #timothy 17
names = {"timothy": 17,"jane":12,"john":21,"peter":25}
n = {}
for clave, valor in names.items():
    n[valor] = clave
print(n)
lista_edades = list(n.keys())
lista_edades.sort()
for edad in lista_edades:
    nombre = n[edad]
    print("{} tiene una edad de: {}".format(nombre, edad))


texto = ''' por que es hermoso ser joven? ¿Por que el sueño de la juventud perenne? Me parece que son dos los elementos determinantes. La juventud tiene todavia el futuro por delante; todo es futuro, tiempo de esperanza. El futuro esta lleno de promesas.
Para ser sinceros, debemos decir que para muchos el futuro también se presenta oscuro, sembrado de amenazas. Hay incertidumbre: ¿encontrare un puesto de trabajo?, ¿encontrare una vivienda?, ¿encontrare el amor?, ¿cual sera mi verdadero futuro?
Y ante estas amenazas, el futuro tambien puede presentarse como un gran vacio. Por eso, hoy muchos quieren detener el tiempo, por miedo a un futuro en el vacio. Quieren aprovechar al maximo inmediatamente todas las bellezas de la vida. Y asi el aceite en la lampara se consuma cuando la vida deberia comenzar. Por eso es importante elegir las verdaderas promesas, que abren al futuro, incluso con renuncias'''
#print(texto)
'''
 Escriba la siguiente función
1. contar_ocurrencias(mensaje)
Esta función retorna un diccionario cuyas claves son las palabras del mensaje y cuyos valores son el numero de veces que cada palabra se repite en el texto.
2. top_k(cont_words,k)
Recibe un diccionario de palabras
Retorna las k palabras que más se repiten en el diccionario
Por ejemplo, si k=5, retorna la lista de las 5 palabras más populares
'''
def contar_ocurrencias(mensaje):
    d = {} 
    abecedario = "abcdefghijklmnñopqrstuvwxyz" 
    lista_palabras = mensaje.strip().lower().split(" ") #convierto en minusculas y separo por un espacio
    for palabra in lista_palabras: #recorro la lista de la linea anterior por medio de sus elementos
        palabra_limpia = "" #"por"
        for caracter in palabra: #recorro cada caracter de esa palabra
            if caracter in abecedario:
                palabra_limpia += caracter
        d[palabra_limpia] = d.get(palabra_limpia, 0) + 1
    return d
dic = contar_ocurrencias(texto)
print(dic)

def top_k(cont_words, k):
    d = {}
    for clave, valor in cont_words.items():
        d[valor] = clave
    lista_cantidades = list(d.keys())
    lista_cantidades.sort()
    l = []
    for indice in range(k):
        valor_cantidad = lista_cantidades[indice]
        palabra = d[valor_cantidad]
        l.append(palabra)
    return l
print(top_k(dic, 10))
