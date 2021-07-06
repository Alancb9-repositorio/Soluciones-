"""Asuma que tiene una lista T de términos. Un término puede ser una palabra o uno de los siguientes tres símbolos:
punto (.), coma (,) y guión (-). Desarrolle un programa que forme un texto usando las siguientes reglas:
● El texto debe estar compuesto de 73 términos seleccionados aleatoriamente
● El primer término debe ser una palabra
● No se puede seleccionar dos símbolos de manera consecutiva. Si eso pasa, seleccione un nuevo término
aleatoriamente hasta que sea una palabra
● Dos palabras seguidas deben estar separadas por un espacio. Ejemplo: palabra1 palabra2
● La coma debe estar pegada a la palabra a su izquierda y separada por un espacio de la palabra a su derecha.
Ejemplo: palabra1, palabra2
● El guión debe estar pegado a sus dos palabras. Ejemplo: palabra1-palabra2
● El punto debe estar pegado a la palabra de la izquierda y seguido de un salto de línea. Ejemplo: palabra1.
● No elimine términos de la lista T."""
T = ["hola", "la", ",", "casa", "por", "computadora", "mesa", ".", ".", "-","cocina", "el", "calle", "mama", "-",
    "telefono", "la", "lo", "en", "en", "lapiz","internet",",", "iglesia", "pies", "ciudad", "ecuadoer", "de", ".", "universidad", "espol", "los", "las"
    "espacio", "gato", "maria", "alan", "kevin", "-", "."]