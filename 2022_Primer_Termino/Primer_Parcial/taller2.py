compra_boletos = input("Desea comprar boletos? ").lower()
obras = ["montesco y su señora", "mamma mia!", "antonie"]
precios = [15, 35, 30]
subtotal = 0
descuento = 0
eligio = 0
if compra_boletos == "si":
    print("******TEATRO SANCHEZ AGUILAR******\n"
          "Bienvenido, las obras disponibles son:\n"
          "Titulo                          costo"
          "Montesco y su señora            $15\n"
          "Mamma mia!                      $35\n"
          "Antonie                         $30\n")
    obras = input("Estimado cliente ingrese la o las obras a las que desea ir.\n"
                  "En caso de ser mas de una, realice el ingreso separado por comas: ").lower()
    if "," in obras:
        lista = obras.split(",")
        if len(lista) == 2:
            cant_entradas = int(input("Cuantos boletos desea para {}".format(lista[0])))
            if cant_entradas > 0:
                subtotal += cant_entradas * precios[obras.index(lista[0])]
                eligio += 1
            else:
                print("No eligio el numero de boletos")
            cant_entradas = int(input("Cuantos boletos desea para {}".format(lista[1])))
            if cant_entradas > 0:
                subtotal += cant_entradas * precios[obras.index(lista[1])]
                eligio += 1
            else:
                print("No eligio el numero de boletos")
        elif len(lista) == 3:
            cant_entradas = int(input("Cuantos boletos desea para {}".format(lista[0])))
            if cant_entradas > 0:
                subtotal += cant_entradas * precios[obras.index(lista[0])]
                eligio += 1
            else:
                print("No eligio el numero de boletos")
            cant_entradas = int(input("Cuantos boletos desea para {}".format(lista[1])))
            if cant_entradas > 0:
                subtotal += cant_entradas * precios[obras.index(lista[1])]
                eligio += 1
            else:
                print("No eligio el numero de boletos")
            cant_entradas = int(input("Cuantos boletos desea para {}".format(lista[2])))
            if cant_entradas > 0:
                subtotal += cant_entradas * precios[obras.index(lista[2])]
                eligio += 1
            else:
                print("No eligio el numero de boletos")
    else:
        cant_entradas = int(input("Cuantos boletos desea para {}".format(obras.capitalize()))
        if cant_entradas > 0:
            subtotal += cant_entradas * precios[obras.index(lista[2])]
        eligio += 1
        else:
            print("No eligio el numero de boletos")   
    if eligio > 0:
        descuento = input("Tiene codigo de descuento? ").lower()
        if descuento == "si":
            codigo = input("Ingrese el codigo de descuento: ")
            if codigo == "TSATEATRO" or codigo == "TSAGYE":
                descuento = 0.15
        total = subtotal - (subtotal * descuento) + (subtotal * 0.12)
        print("El subtotal es de: {}".format(subtotal))
        print("El descuento es de: {}".format(subtotal * descuento))
        print("El iva(12%) es de: {}".format(subtotal * 0.12))
        print("El total a pagar es de: {}".format(total))
else:
    print("Muchas gracias vuelva pronto")
print("Fin del programa.")