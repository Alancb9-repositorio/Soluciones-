"""EJERCICIO DE EXAMEN 7

Un asistente de médico tiene la tarea de generar un informe de indicadores a partir del resultado de un examen de sangre  
que lo recibe como una cadena de texto.
Los indicadores, por ejemplo: INR, WBC, RBC, TA, etc.,  se pueden identificar por estar siempre en mayúsculas. Todo 
indicador va seguido de un espacio, un número con decimales, otro espacio y las unidades de medida. Al final del reporte 
se encuentra el nombre del médico responsable."""

"""Nota: 
- La cantidad de indicadores puede variar. Los puntos no solo aparecen en los decimales, sino también para separar 
  párrafos o en otras ocasiones como las direcciones de e-mail.

- Escriba un programa que muestre la información desglosada, el nombre del médico, una recomendación mostrada como doble 
  asterisco en el indicador y descrita al final

- Se recomienda al paciente ir al endocrinólogo si su nivel de azúcar (BGT), está por encima de los 150 mmol/dL."""
"""Ejemplo:

INFORME DE LABORATORIO
**********************
INR	     1.25 	segundos
BGT 	   180.12 	mmol/dL
HGB	    13		g/dL
ESR	     3.2 	mm/hora
RBC	4000024.2 	cel/ul
TA 	     1.5 	ng/dL
WBC 	123233.23 	cel/uL
Médico: Juan Pozo

** Su nivel de azúcar es alto, se recomienda ir al endocrinólogo ."""

#Ejemplos:
#resultado = "Resultado de Laboratorio 'Su Salud' Nombre del paciente: José Aimas E-mail del paciente: jose.aimas@gmail.com Resultados del laboratorio: INR 1.25 segundos BGT 180.12 mmol/dL HGB 13 g/dL ESR 3.2 mm/hora RBC 4000024.2 cel/ul TA 1.5 ng/dL WBC 123233.23 cel/uL. Los valores de éste informe no representan un diagnóstico. Firma médico responsable: Dr. Juan Pozo"
resultado = "Resultado de Laboratorio 'Sana' Nombre del paciente: Ginger Irene Cruz Jurado Edad: 25 años E-mail: giircrju@espol.edu.ec Resultados: Azucar BGT 180.12 mmol/dL Hemoglobina HGB 13 g/dL Hormonal TA 1.5 ng/dL Médico responsable Dra. Karina Elizabeth Plaza"
lista = resultado.split()
d = {} #{"indicador":cantidad....., "Medico":"nombre del medico"}
print("INFORME DE LABORATORIO")
print("**********************")
for indice in range(len(lista)):
    if lista[indice].isupper():
        d[lista[indice]] = float(lista[indice + 1])
        print("{}           {}          {}".format(lista[indice], lista[indice + 1], lista[indice + 2]))
    if lista[indice] == "Dra." or lista[indice] == "Dr.":
        print("Medico: {}".format(" ".join(lista[indice + 1:])))
if d["BGT"] > 150:
    print("** Su nivel de azúcar es alto, se recomienda ir al endocrinólogo.")

