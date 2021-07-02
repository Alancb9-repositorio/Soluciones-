'''En el diccionario de visitas se da información sobre las personas que han visitado un importante laboratorio de investigación.'''

'''Escriba las siguientes funciones:
1.	num_visitantes(dic, mes,year)
Recibe un diccionario con el formato del diccionario datos y el nombre de un mes ("Enero","Febrero",...).
Devuelve un diccionario cuyas claves son los países y cuyo valor son el número de personas de ese pais que estuvieron de visita en el mes y año indicado.
Ejemplo
num_visitantes(datos,"Octubre",2019)
devolvería
{'Italia': 3, 'Francia': 2, 'Argentina': 1, 'Alemania': 1, 'España': 1, Japon:1}
2.	visita_por_pais(dic ,continentes, mes,year)
Recibe el diccionario de visitas y el de continentes, además recibe el nombre de un mes y el año.
Devuelve un diccionario con el nombre del continente como clave y el numero de visitantes de ese continente como valor.

Programa Principal
1.	Pida al usuario que ingrese meses hasta ingresar la palabra "fin". Almacene esos meses en una lista.
2.	Muestre cuántas personas de cada continente estuvieron de visita en el laboratorio en octubre de 2019.'''

#1
def num_visitantes(dic, mes, year):
    d = {}
    fecha_entrada = dic["fecha_entrada"]
    paises = dic["Paises"]
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio" , "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    numero_mes = str(meses.index(mes.lower()) + 1)
    if len(numero_mes) == 1:
        numero_mes = "0" + str(meses.index(mes.lower()) + 1)  
    for indice in range(len(fecha_entrada)): #0,1,2,3,4,5,6,7,8
        if (numero_mes in fecha_entrada[indice]) and (year in fecha_entrada[indice]):
            d[paises[indice]] = d.get(paises[indice], 0) + 1
    return d

def visita_por_pais(dic, continentes, mes, year):
    d = {}
    fecha_entrada = dic["fecha_entrada"]
    paises = dic["Paises"]
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio" , "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    numero_mes = str(meses.index(mes.lower()) + 1)
    if len(numero_mes) == 1:
        numero_mes = "0" + str(meses.index(mes.lower()) + 1)
    for indice in range(len(fecha_entrada)):
        if (numero_mes in fecha_entrada[indice]) and (year in fecha_entrada[indice]):
            for clave_continente, valor in continentes.items():
                if paises[indice] in valor:
                    d[clave_continente] = d.get(clave_continente, 0) + 1
    return d


datos={"Visitantes": ["Juan","Pietro","Michelle","Rafaello","Andres","Corinna","Edith","Teresa","Dominique"],
       "fecha_entrada":["26-06-2019","02-10-2019","06-10-2019","18-05-2020","15-10-2020","06-10-2019","01-10-2019","02-11-2019","01-10-2019"], 
       "Paises": ["Italia","Francia", "Argentina", "Italia", "Francia", "Italia", "Alemania", "España","Japon"]}
continentes={"America":["Estados Unidos","Argentina","Ecuador","Peru"],
             "Europa": ["Portugal","Francia","Italia","Alemania"],
             "Asia":["India","China","Japon"]}
respuesta = num_visitantes(datos,"octubre", "2019")
print(respuesta)
print("----------------------------------------------------------------")
respuesta2 = visita_por_pais(datos, continentes, "octubre", "2019")
print(respuesta2)


