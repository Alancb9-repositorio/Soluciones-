"""
Una empresa registra los servicios de internet visitados por los empleados y los minutos de navegacion en una lista semejante 
a la mostrada. Cada registro se almacena usando una cadena con el formato: "empleado|sitio visitado|horas":
"""
#Escriba las siguientes funciones:
"""
1. calcula_tiempo(visitados,trabajo)
Recibe las listas con el formato mostrado arriba
Devuelve un diccionario cuyas claves son los nombres de los empleados, el valor asociado a la clave es una lista de dos 
elementos que representan el numero de horas que el empleado invirtio en sitios de trabajo y el numero de horas que el 
empleado invirtio en otros sitios.
2. empleado_trabajo(visitados,trabajo)
Recibe las listas con el formato mostrado arriba
Devuelve el nombre del empleado que mas horas invirtio en sitios que no son de trabajo y el numero de horas correspondiente.
"""

#Programa Principal
"""
1. Muestre el nombre del empleado que mas horas invirtio en sitios de trabajo.
2. Muestre el nombre del empleado que mas horas invirtio para los siguientes sitios: "twitter.com", eluniverso.com"""

visitados= ["maria2|www.facebook.com|160","xavi7|www.eluniverso.com|50","jose15|www.sri.gob.ec|30",
            "maria2|www.twitter.com|30","xavi7|www.inec.gob.ec|10","maria2|www.espol.edu.ec|50",
            "jose15|www.sri.gob.ec|120","xavi7|www.sri.gob.ec|20","maria2|www.twitter.com|20",
            "jose15|www.eluniverso.com|30"]

trabajo= ["www.espol.edu.ec","www.inec.gob.ec","www.sri.gob.ec"]
#Funcion 1
#d = {"nombre_empleado":[hora sitios de trabajo, hora sitios que no son trabajo]...}
def calcula_tiempo(visitados, trabajo):
    d = {} #{"maria2": [0,160]}
    for informacion in visitados: #1 informacion = "maria2|www.facebook.com|160"
        lista = informacion.split("|") #lista = ["maria2", "www.facebook.com", "160"]
        nombre_empleado = lista[0] #nombre_empleado = "maria2"
        sitio_web = lista[1]    #sitio_web = "www.facebook.com"
        hora = lista[2]     #hora = "160"
        d[nombre_empleado] = d.get(nombre_empleado, [0, 0]) #d["maria2"] = [0,0]
        if sitio_web in trabajo: #"www.facebook.com" in ["www.espol.edu.ec","www.inec.gob.ec","www.sri.gob.ec"]
            d[nombre_empleado][0] = d[nombre_empleado][0] + int(hora)
        else:
            d[nombre_empleado][1] = d[nombre_empleado][1] + int(hora)   #d["maria2"][1] = 160
    return d
tiempo_calculado = calcula_tiempo(visitados, trabajo)
print(tiempo_calculado)
#Funcion 2, primera forma de hacerlo
def empleado_trabajo1(visitados, trabajo):
    d = calcula_tiempo(visitados, trabajo) #d = {'maria2': [50, 210], 'xavi7': [30, 50], 'jose15': [150, 30]}
    nombre_empleado = "" #nombre_empleado = ""
    horas_no_trabajo = 0    #horas_no_trabajo = 0
    for clave, valor in d.items(): #clave = "maria2" valor = [50,210]
        if valor[1] > horas_no_trabajo: #210 > 0 
            horas_no_trabajo = valor[1] #horas_no_trabajo = 210
            nombre_empleado = clave #nombre_empleado = "maria2"
    return nombre_empleado, horas_no_trabajo
#Funcion 2, segunda forma de hacerlo
def empleado_trabajo2(visitados, trabajo):
    d = calcula_tiempo(visitados, trabajo)
    nombre_empleado = []
    horas_no_trabajo = []
    for clave, valor in d.items():
        nombre_empleado.append(clave)
        horas_no_trabajo.append(valor[1])
    maximo = max(horas_no_trabajo)
    indice_maximo = horas_no_trabajo.index(maximo)
    nombre_maximo = nombre_empleado[indice_maximo]
    return nombre_maximo, maximo

nombre1, horas1 = empleado_trabajo1(visitados, trabajo)
print("El empleado(a) {} tuvo {} horas en sitios que no son de trabajo".format(nombre1, horas1))
print("------------------------------------------------------------------------------------------")
nombre2, horas2 = empleado_trabajo2(visitados, trabajo)
print("El empleado(a) {} tuvo {} horas en sitios que no son de trabajo".format(nombre2, horas2))


