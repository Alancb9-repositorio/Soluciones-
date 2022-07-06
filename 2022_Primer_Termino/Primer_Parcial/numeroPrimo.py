numero = input("Ingrese un numero entero: ") #numero = "5"    
while not(numero.isdigit()):    
    print("El dato es erroneo.")
    numero = input("Ingrese nuevamente un numero entero: ")
x = 2   #x = 4
es_primo = 0 #es_primo = 5 
while es_primo < int(numero):    #5 < 5 = False
    cont = 0    #cont = 2
    for i in range(1, x + 1):    #(1, 4) = (1,2,3)     i = 3
        if x % i == 0:    #0 == 0 = True
            cont += 1    #cont += 1
    if cont == 2: #2 == 2 = True
        print(x) #3
        es_primo += 1 #es_primo += 1
    x += 1


# La empresa «FICTICIA S.L.» a fecha de 1 de Enero presenta en su contabilidad los siguientes elementos patrimoniales, con sus correspondientes saldos (en euros):

# saldos = [ 'Caja 1.000€ Activo corriente', 'Préstamo bancario a 2 años 30.000€ Pasivo no corriente', 'Facturas pendientes de clientes a c/p 13.000€ Activo corriente', 'Equipos informáticos 6.000€ Activo no corriente', 'Local (oficina) 60.000€ Activo no corriente', 'Vehículo de la empresa 17.000€ Activo no corriente', 'Dinero en cuenta corriente 25.000€ Activo corriente', 'Letras pendientes de pago c/p 8.000€ Pasivo corriente', 'Mobiliario 13.000€ Activo no corriente', 'Maquinaria 10.000€ Activo no corriente', 'Facturas pendientes de pago c/p 22.000€ Pasivo corriente', 'Existencias 8.000€ Activo corriente']

# Haga un programa que muestre el total de Activo corriente, Activo no corriente, Activo (Activo corriente + Activo no corriente), Pasivo corriente, Pasivo no corriente, y Pasivo (Pasivo corriente + Pasivo no corriente).

# Muestre la cuenta con mayor valor del Activo y del Pasivo, con su respectivo valor.

# Al final, muestre el valor del Patrimonio (Activo - Pasivo).  

#Solucion
# saldos = [ 'Caja 1.000€ Activo corriente', 'Préstamo bancario a 2 años 30.000€ Pasivo no corriente', 'Facturas pendientes de clientes a c/p 13.000€ Activo corriente', 'Equipos informáticos 6.000€ Activo no corriente', 'Local (oficina) 60.000€ Activo no corriente', 'Vehículo de la empresa 17.000€ Activo no corriente', 'Dinero en cuenta corriente 25.000€ Activo corriente', 'Letras pendientes de pago c/p 8.000€ Pasivo corriente', 'Mobiliario 13.000€ Activo no corriente', 'Maquinaria 10.000€ Activo no corriente', 'Facturas pendientes de pago c/p 22.000€ Pasivo corriente', 'Existencias 8.000€ Activo corriente']
# activo_corriente = 0
# activo_no_corriente = 0
# pasivo_corriente = 0
# pasivo_no_corriente = 0
# activos = []
# cuentas_activos = []
# pasivos = []
# cuentas_pasivos = []
# for elemento in saldos:    #elemento = 'Préstamo bancario a 2 años 30.000€ Pasivo no corriente'
#     datos, caracteristica = elemento.split("€ ")    #["Préstamo bancario a 2 años 30.000", "Pasivo no corriente"]
#     cantidad = int(datos.split(" ")[-1].replace(".", "")) #["Préstamo","bancario", "a", "2", "años", "1.000"] = "1.000" = "1000" = 1000
#     nombre = " ".join(datos.split(" ")[:-1])    #nombre = ["Préstamo","bancario", "a", "2"] = "Préstamo bancario a 2 años"
#     if caracteristica == "Activo corriente":
#         activo_corriente += cantidad
#     elif caracteristica == "Activo no corriente":
#         activo_no_corriente += cantidad
#     elif caracteristica == "Pasivo corriente":
#         pasivo_corriente += cantidad
#     elif caracteristica == "Pasivo no corriente":
#         pasivo_no_corriente += cantidad
#     if "Activo" in caracteristica:
#         activos.append(cantidad)
#         cuentas_activos.append(nombre)
#     else:
#         pasivos.append(cantidad)
#         cuentas_pasivos.append(nombre)    
# maximo_activo = max(activos)
# maximo_pasivo = max(pasivos)
# indice_max_activo = activos.index(maximo_activo)
# indice_max_pasivo = pasivos.index(maximo_pasivo)
# nombre_max_activo = cuentas_activos[indice_max_activo]
# nombre_max_pasivo = cuentas_pasivos[indice_max_pasivo]
# patrimonio = sum(activos) - sum(pasivos)
# print("La suma de activos corrientes : {}".format(activo_corriente))
# print("La suma de activos no corrientes : {}".format(activo_no_corriente))
# print("La suma de pasivos corrientes : {}".format(pasivo_corriente))
# print("La suma de pasivos no corrientes : {}".format(pasivo_no_corriente))
# print("La suma de activos es: {}".format(activo_corriente + activo_no_corriente))
# print("La suma de pasivos es: {}".format(pasivo_corriente + pasivo_no_corriente))
# print("El nombre de la cuenta con mayor activo es {}, con un valor de {} ".format(nombre_max_activo, maximo_activo))
# print("El nombre de la cuenta con mayor pasivo es {}, con un valor de {} ".format(nombre_max_pasivo, maximo_pasivo))
# print("El patrimonio es: {}".format(patrimonio))

# n1 = input("Ingrese el primer valor: ") #n1 = "hola"
# while not(n1.isdigit()):    #"4".isdigit() = not(True) = False
#     print("Dato equivocado.")
#     n1 = input("Ingrese nuevamente el primer valor: ") #n1 = "4"

# n2 = input("Ingrese el segundo valor: ")
# print("La suma es: {}".format(int(n1) + int(n2)))
