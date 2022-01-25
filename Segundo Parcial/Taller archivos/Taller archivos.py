'''Para el siguiente taller usted trabajará con dos archivos adjuntos a este documento 
llamados cuentas.txt y informacion.txt.

    • cuentas.txt tiene los datos de usuario y clave de las cuentas del sistema en cada línea
    • informacion.txt tiene los datos personales de las cuentas del sistema en cada línea

El único nexo entre ambos archivos es el nombre de usuario. A continuación:

Crear un sistema de registro de usuario, el sistema deberá realizar lo siguiente:

Crear una función llamada PresentarMenu(), esta función presentará por pantalla el 
siguiente menú, y retornar la opción válida, verificar con una tupla que el usuario 
seleccione únicamente las opciones permitidas, es decir 1 o 2:

    1. Iniciar sesión
    2. Crear usuario

Si el usuario escoge la opción 1, el sistema solicitará un usuario y una clave. Usted deberá 
crear la función IniciarSesion(usuario, clave) la cual recibe el usuario y clave que el 
usuario ingresó y debe retornar un diccionario con la información de dicho usuario. 
Usted debe imprimir este diccionario por pantalla.

Ejemplo:
IniciarSesion(‘fmalo’, ‘prueba’) retornará el siguiente diccionario: -→

{‘1234567890’: (’Frank’, ’malo’, 31)}

Si el usuario no existe o la clave es incorrecta debe mostrar un mensaje de error y 
devolver un diccionario vacío.

Si el usuario escoge la opción 2, el sistema debe solicitar un usuario, una clave, una 
cédula, un nombre, un apellido y una edad y guardarlo en los archivos correspondientes.

En la opción 2 de Crear Usuario, usted debe validar que el usuario no haya sido 
previamente creado por medio del usuario, es decir el usuario nuevo no debe existir en 
ninguno de los dos archivos.'''

def PresentarMenu():
    print("1. Iniciar sesión.\n"
          "2. Crear usuario.")
    tupla_opciones = ("1", "2")
    dato_usuario = input("Estimado usuario ingrese una de las opciones: ") #"1"
    while dato_usuario not in tupla_opciones:
        print("DATO INCORRECTO.")
        dato_usuario = input("Estimado usuario ingrese nuevamente una de las opciones: ")
    return int(dato_usuario)

def IniciarSesion(usuario, clave):
    d = {}
    f = open("cuentas.txt", "r")
    lista_datos = f.read().strip().split("\n")
    f.close()
    usuario_clave = usuario + "@" + clave
    if usuario_clave not in lista_datos:
        print("El usuario o la contrasena son incorrectos.")
        return d
    else:
        f = open("informacion.txt", "r")
        for line in f:
            usuario_archivo, cedula, nombre, apellido, edad = line.strip().split("$")
            if usuario == usuario_archivo:
                d[cedula] = (nombre, apellido, int(edad))
                f.close()
                return d

opcion_usuario = PresentarMenu()
if opcion_usuario == 1:
    usuario = input("Ingrese un usuario: ")
    clave = input("Ingrese una clave: ")
    dicc = IniciarSesion(usuario, clave)
    print(dicc)
else:
    usuario = input("Ingrese un usuario: ")
    f = open("cuentas.txt", "r")
    l_usuarios = []
    for line in f:
        usu_archivo, clave = line.strip().split("@")
        l_usuarios.append(usu_archivo)
    f.close()
    while usuario in l_usuarios:
        print("El usuario ingresado ya esta en uso.")
        usuario = input("Ingrese nuevamente un usuario: ")
    clave = input("Ingrese una clave: ")
    cedula = input("Ingrese una cedula: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese un apellido: ")
    edad = input("Ingrese la edad: ")
    f = open("cuentas.txt", "a")
    f.write(usuario + "@" + clave + "\n")
    f.close()
    f = open("informacion.txt", "a")
    f.write(usuario + "$" + cedula + "$" + nombre + "$" + apellido + "$" + edad + "\n")
    #f.write("{}${}${}${}${}\n".format(usuario, cedula, nombre, apellido, edad))
    f.close()