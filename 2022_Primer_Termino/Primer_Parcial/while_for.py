#Estructuras de control iterativas(LAZOS)
#For
# x1= input("Ingrese un numero: ")
# x2= input("Ingrese un numero: ")
# x3= input("Ingrese un numero: ")
# x4= input("Ingrese un numero: ")
# x5= input("Ingrese un numero: ")

#for variable_iteracion in coleccion:
#la coleccion puede una lista, string, una secuencia(range)
#range(1, 9)   (1,2,3,4,5,6,7,8)
#range(5)    (0,1,2,3,4)
# for i in range(5):    #(0,1,2,3,4) i =2    iteracion = 1
#     print(i)
#     x1= input("Ingrese un numero: ")    #x1 = 10
# lista = [1,2,3,4,5]    #lista = [1,2,3,4,5]
# for numero in lista:    #numero = 3     lista = [1,2,3,4,5]
#     print(numero * 2)    #print(3 * 2) >>> 6
# print("fin del programa")

#Ejercicio1
# lista_numeros = [1,2,3,4,5,6,7,8,9,10]
# for numero in lista_numeros:
#     cuadrado = numero ** 2
#     print(cuadrado)

#contador
# x = 10
# x = x + 2    #x += 1
# x += 2
# x += 2
# print(x)

#acumulador
# y = 1
# y *= 2    #y = 2
# y *= 2    #y = 4
# y *= 2    #y = 8
# print(y)
# lista_numeros = [1,2,3,4,5,6,7,8,9,10]
# suma = 0    #suma = 6
# for numero in lista_numeros: #lista_numeros = [1,2,3,4,5,6,7,8,9,10]    numero = 3
#     suma += numero    #suma = 6
# print(suma)

# lista = ["a", "b", 100, "d", ["hola", "casa"]]
# for indice in range(len(lista)):    #range(4) = (0,1,2,3,4)
#     print("el indice {} tiene como elemento {}".format(indice, lista[indice]))

# l = ["hola", "casa", 9, "gato"]
# for indice, elemento in enumerate(l):
#     print(indice, elemento)


#sintaxis
#While condicion o condiciones:
    #codigo
    #codigo
    #codigo
# from random import randint
# suma = 0    #suma = 34
# while suma <= 30:    #34 <= 30: False
#     numero_aleatorio = randint(1,10)    #numero_aleatorio = 5
#     print("el numero aleatorio es: ",numero_aleatorio)
#     suma += 2    #suma = 34
#     print("la suma es: ", suma)
# print(suma)

# from random import randint
# numero_aleatorio = randint(1, 20)
# print(numero_aleatorio)
# numero_usuario = ""
# while (numero_usuario != numero_aleatorio) and (numero_usuario != "fin"):    #15 != 15 or 15 != "fin"
#     numero_usuario = input("Ingrese un numero del 1  al 20: ")
#     if numero_usuario != "fin":
#         numero_usuario = int(numero_usuario)
#     if numero_usuario == numero_aleatorio:    
#         print("ADIVINO!")
#     elif numero_usuario != numero_aleatorio and :
#         print("VUELVA A INTENTARLO")
# print("fin del programa")

