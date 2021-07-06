"""
LECCION 3
"""
#Escriba las siguientes funciones
"""
1.agregar(d,cedula,nombre,deporte) Esta funcion recibe el diccionario d, los str cedula, nombre, deporte y agrega la informacion
al diccionario d. Si el usuario ya existe, solamente agrega la informacion del deporte. Si el usuario no existe, cree la estructura
"cedula":[nombre,set].

2. diferentes(d,cedula) Esta funcion recibe el diccionario d, y el str cedula.
Retorna cual es el usuario que mas "difiere" del usuario dado.
Para determinar cual es el ususario que mas difiere debe calcular cuantos deportes NO tienen en comun en sus pertenencias .
Por ejemplo: Paul Martin y Martin Roman difieren en los siguientes deportes: natacion, aledrez. El numero de deportes en el que
difieren es dos.
"""
personas= {"1012345678": ["Paul Martinez",{"natacion","voleyball","ciclismo"}],
           "1007812345": ["Peter Roman",{"ciclismo","voleyball","ajedrez"}],
           "1000067123": ["Mathew Sinal",{"atletismo","voleybal","basket"}],
           "1009812345": ["Kevin Carriel",{"ping-pong","gimnasia","basket"}]
           }

#1
def agregar(d, cedula, nombre, deporte): #cedula = "0955832514" nombre = "Melanie Reyes" deporte = "Dormir"
    d[cedula] = d.get(cedula, [nombre, set()])  #d["0955832514"] = ["Melanie Reyes", set()]
    d[cedula][1] = d[cedula][1] | {deporte} #d["0955832514"][1] = {"Dormir"}
agregar(personas, "0955832514", "Melanie Reyes", "Dormir")
agregar(personas, "0955832514", "Melanie Reyes", "Estudiar")
print(personas)

#2
def diferentes(d, cedula):
    deportes = d[cedula][1]
    nombre = ""
    cantidad = 0
    for identificacion, lista in d.items():
        if identificacion != cedula:
            conjunto_deportes = lista[1]
            diferencia_simetrica = deportes ^ conjunto_deportes
            longitud = len(list(diferencia_simetrica))
            if longitud > cantidad:
                nombre = lista[0]
                cantidad = longitud
    return nombre
persona = diferentes(personas, "1012345678")
print(persona)