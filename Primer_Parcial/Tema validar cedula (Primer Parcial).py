"""Escriba una función validar(cédula) que valide si un número de cédula ingresado es válido.
Para validar una cédula de identidad ecuatoriana el proceso es el siguiente:

Ejemplo:	0909407173
El décimo es dígito verificador que se validará	3 es el dígito verificador
Se trabaja con los primeros 9 dígitos de la cédula	090940717
Cada dígito de posición impar se lo duplica, si el resultado es mayor que nueve se resta nueve	090980515
Se suman todos los resultados de posición impar	0+0+8+5+5 = 18
Se suman todos los dígitos de posición par	9+9+0+1 = 19
Se suman los dos resultados.	18+19 = 37
Se resta de la decena inmediata superior; en caso de ser 10, el resultado se vuelve a restar 10	40 – 37 = 3
Este es el verificador “calculado”	3
Si el dígito verificador es igual al verificador “calculado”, la cédula es válida, caso contrario es falsa	3 = 3 Cédula válida"""

def validar(cedula):
    suma_impar = 0
    suma_par = 0
    for indice in range(len(cedula) - 1):
        if (indice + 1) % 2 == 1:
            duplicado = int(cedula[indice]) * 2
            if duplicado > 9:
                duplicado -= 9
            suma_impar += duplicado
        else:
            suma_par += int(cedula[indice])
    total = suma_impar + suma_par
    verificador = (total - (total % 10) + 10) - total
    return cedula[-1] == str(verificador)
print(validar("0928055698"))