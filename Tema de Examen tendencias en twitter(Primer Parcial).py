#a
def cuentaTopics(tendencias, listaFechas):          #fechas = ['08-22-2016', '08-25-2016', '08-27-2016', '08-28-2016']
    d = {} # {'#Rio2016':1, "#BSC":1, "#ECU":2, "#ALAN":1, "#GYE":1, "#BRA":1}
    for clave, valor in tendencias.items(): #clave = '08-25-2016' valor = {'#GYE', '#BRA', "#ECU"}
        if clave in listaFechas: 
            for hashtag in valor: #hashtag = "#ECU"
                d[hashtag] = d.get(hashtag, 0) + 1  #   d["#ECU"] = 2
    return d
#b
def reportaTrending1(tendencias, listaFechas):
    resultado = tendencias[listaFechas[0]] #tendencias['08-22-2016'] = {'#Rio2016', '#BSC', '#ECU', "#ALAN"}
    for fecha in listaFechas:
        conjunto_hashtags = tendencias[fecha]    #{'#Rio2016', '#ECU', '#BIGMONKEY', '#ALAN'}
        interseccion = resultado & conjunto_hashtags #{'#Rio2016', '#BSC', '#ECU', "#ALAN"} & {'#Rio2016', '#ECU', '#BIGMONKEY', '#ALAN'} = {"#ALAN", "#ECU"}
        resultado = interseccion #{"#ALAN", "#ECU"}
    for h in resultado:
        print(h)
def reportaTrending2(tendencias, listaFechas):
    respuesta = set() #{}
    for fecha in listaFechas: # 1 '08-22-2016' 2 '08-25-2016' 3 '08-27-2016' 4 '08-28-2016'
        respuesta = respuesta | tendencias[fecha] #{'#Rio2016', '#GYE', '#BRA', '#YoSoyEspol', '#BSC', "#ALAN", "#ECU"} | {'#Rio2016', '#ECU', '#BIGMONKEY', '#ALAN'} = {'#Rio2016', '#GYE', '#BRA', '#YoSoyEspol', '#BSC', '#ECU', '#BIGMONKEY', '#ALAN'}
    for h in respuesta: #{'#Rio2016', '#GYE', '#BRA', '#YoSoyEspol', '#BSC', '#ECU', '#BIGMONKEY', '#ALAN'}
        print(h)
def reportaTrending3(tendencias, fecha1, fecha2):
    f1 = tendencias[fecha1]
    f2 = tendencias[fecha2]
    diferencia_simetrica = f1 ^ f2
    for h in diferencia_simetrica:
        print(h)
#Programa principal
tendencias = {
 '08-22-2016':{'#Rio2016', '#BSC', '#ECU', "#ALAN"}, 
 '08-25-2016':{'#GYE', '#BRA', "#ECU"}, 
 '08-27-2016':{'#YoSoyEspol', '#GYE', '#BSC', "#ALAN", "#ECU"},
 '08-28-2016':{'#Rio2016', '#ECU', '#BIGMONKEY', '#ALAN'}
 }
fechas = ['08-22-2016', '08-25-2016', '08-27-2016', '08-28-2016']
topics = cuentaTopics(tendencias, fechas)
print(topics)
reportaTrending1(tendencias, fechas)
print("-----------------------------------------")
reportaTrending2(tendencias, fechas)
print("-----------------------------------------")
reportaTrending3(tendencias, '08-25-2016', '08-28-2016')
