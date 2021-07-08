"""TEMA 2. (50 PUNTOS) Para administrar la nueva matriz energética del Ecuador,
se dispone de un diccionario con la información de las plantas de energía y las ciudades que atienden cada una.

Cada ciudad tiene: una tupla con los consumos mensuales (12) del año en megavatios-hora (MWh) y la tarifa de consumo en dólares por megavatio-hora (MWh)
que le cobra la planta eléctrica.

Una ciudad puede estar servida por más de una planta eléctrica. No todas las ciudades son servidas por todas las plantas eléctricas."""
consumo_energia = {
    'Coca Codo Sinclair': {
        'Quito': { 'consumos':(400, 432, 213),'tarifa': 65},
        'Guayaquil': { 'consumos': (120, 55, 32, 70, 50, 80, 755, 82, 93, 60, 120, 25),'tarifa': 84},
        },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 200),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587),'tarifa': 79},
        'Loja': { 'consumos': (50, 32, 32, 40),'tarifa': 32},
        },
} 
"""Además, dispone del siguiente diccionario con información de ciudad por región :"""
""" informacion = {
    'costa': ('Guayaquil', 'Manta', …),
    'sierra': ('Quito', 'Ambato', …),
    'oriente': ('Tena', 'Nueva Loja', …),
    } """
"""Implemente lo siguiente:
1.Una función total_anual(consumo_energia, planta, ciudad) que recibe el diccionario consumo_energia, 
el nombre de una planta y el nombre de una ciudad. La función debe calcular y retornar el total anual de megavatios-hora servido por planta a ciudad. (7 puntos)

2.Una función total_plantas_ciudad(consumo_energia, ciudad) que recibe el diccionario consumo_energia y el nombre de una ciudad.
La función debe devolver un diccionario cuyas claves corresponden a los nombres de las plantas generadoras que proveen energía a ciudad
y los valores corresponden al total anual de megavatios-hora servido por cada planta a ciudad. (13 puntos)

3.Una función megavatios_hora(consumo_energia, informacion) que recibe el diccionario consumo_energia y el diccionario informacion. 
La función retorna el total anual de megavatios-hora consumido por todas las ciudades de la región COSTA. (15 puntos)
"""
#literal 1
def total_anual(consumo_energia, planta, ciudad):
    planta = consumo_energia[planta]    #{"ciudad1":{"consumos": (cantidad1, cantidad2,...), "tarifa": cantidad1}, "ciudad2":{"consumos": (cantidad1, cantidad2,...), "tarifa": cantidad2},....}
    ciudad = planta[ciudad] #{"consumos": (cantidad1, cantidad2,...), "tarifa": cantidad1}
    total = 0
    for cantidad in ciudad["consumos"]:
        total += cantidad
    return total

#Literal2
def total_plantas_ciudad(consumo_energia, ciudad):
    d = {}
    for planta, dic_ciudades in consumo_energia.items():
        tupla = dic_ciudades[ciudad]["consumos"]
        suma = 0
        for cantidad in tupla:
            suma += cantidad
        d[planta] = suma
    return d

#Literal3
def megavatios_hora(consumo_energia, informacion):
    suma = 0
    for planta, dicionario_ciudades in consumo_energia.items():
        for ciudad in dicionario_ciudades.keys():
            if ciudad in informacion["costa"]:
                suma += total_anual(consumo_energia, planta, ciudad)
    return suma   

resultado = total_anual(consumo_energia, 'Coca Codo Sinclair', 'Guayaquil')
print(resultado)

resultado2 = total_plantas_ciudad(consumo_energia, 'Quito')
print(resultado2)

resultado3 = megavatios_hora(consumo_energia, informacion)
print(resultado3)
