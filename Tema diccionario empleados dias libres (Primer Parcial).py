"""#1. Para cada empleado: imprima el numero de dias que tienen disponibles
#2. Dados dos empleados, retorne la lista de dias disponibles que tienen en común
def comun(dic,ced1,ced2):"""

empleados= {
    "103456789": {'name': 'Melissa',
                  'birthday': '06-October',
                  'days_available': ['Monday', 'Tuesday', 'Saturday', 'Sunday']
                 },
    "107893456": {'name': 'Angelica',
                  'birthday': '02-October',
                  'days_available': [ 'Wednesday', 'Thursday', 'Friday']
                 },
    "103459678": {'name': 'Eugenia',
                  'birthday': '13-July',
                  'days_available': ['Monday', 'Tuesday', 'Friday', 'Saturday']
                 },
    "109459678": {'name': 'Carmen',
                  'birthday': '16-July',
                  'days_available': ['Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday']
                  }}

#Literal 1
for identificacion, diccionario in empleados.items():
    print("El empleado(a) {} tiene disponible {} dias".format(diccionario["name"], len(diccionario['days_available'])))
#Literal 2
def comun(dic, ced1, ced2):
    empleado_1 = dic[ced1]["days_available"]
    empleado_2 = dic[ced2]["days_available"]
    interseccion = set(empleado_1) & set(empleado_2)
    return list(interseccion)
resultado = comun(empleados, "107893456", "109459678")
print("Los dias en comun son {}".format(resultado))
