# La empresa «FICTICIA S.L.» a fecha de 1 de Enero presenta en su contabilidad los siguientes elementos patrimoniales, con sus correspondientes saldos (en euros):

# saldos = [ 'Caja 1.000€ Activo corriente', 'Préstamo bancario a 2 años 30.000€ Pasivo no corriente', 'Facturas pendientes de clientes a c/p 13.000€ Activo corriente', 'Equipos informáticos 6.000€ Activo no corriente', 'Local (oficina) 60.000€ Activo no corriente', 'Vehículo de la empresa 17.000€ Activo no corriente', 'Dinero en cuenta corriente 25.000€ Activo corriente', 'Letras pendientes de pago c/p 8.000€ Pasivo corriente', 'Mobiliario 13.000€ Activo no corriente', 'Maquinaria 10.000€ Activo no corriente', 'Facturas pendientes de pago c/p 22.000€ Pasivo corriente', 'Existencias 8.000€ Activo corriente']

# Haga un programa que muestre el total de Activo corriente, Activo no corriente, Activo (Activo corriente + Activo no corriente), Pasivo corriente, Pasivo no corriente, y Pasivo (Pasivo corriente + Pasivo no corriente).

# Muestre la cuenta con mayor valor del Activo y del Pasivo, con su respectivo valor.

# Al final, muestre el valor del Patrimonio (Activo - Pasivo).

saldos = [ 'Caja 1.000€ Activo corriente', 'Préstamo bancario a 2 años 30.000€ Pasivo no corriente', 'Facturas pendientes de clientes a c/p 13.000€ Activo corriente', 'Equipos informáticos 6.000€ Activo no corriente', 'Local (oficina) 60.000€ Activo no corriente', 'Vehículo de la empresa 17.000€ Activo no corriente', 'Dinero en cuenta corriente 25.000€ Activo corriente', 'Letras pendientes de pago c/p 8.000€ Pasivo corriente', 'Mobiliario 13.000€ Activo no corriente', 'Maquinaria 10.000€ Activo no corriente', 'Facturas pendientes de pago c/p 22.000€ Pasivo corriente', 'Existencias 8.000€ Activo corriente']
activo_corriente = []
activo_no_corriente = []
pasivo_corriente = []
pasivo_no_corriente = []
cuentas_activo = []
cuentas_pasivo = []
for elemento in saldos:
    datos, caracteristica = elemento.split("€")
    lista = datos.split(" ")
    cantidad = lista[-1].replace(".", "")
    if caracteristica.strip() == "Activo corriente":
        activo_corriente.append(int(cantidad))
    elif caracteristica.strip() == "Activo no corriente":
        activo_no_corriente.append(int(cantidad))
    elif caracteristica.strip() == "Pasivo corriente":
        pasivo_corriente.append(int(cantidad))
    elif caracteristica.strip() == "Pasivo no corriente":
        pasivo_no_corriente.append(int(cantidad))
    if
activo = activo_corriente + activo_no_corriente
pasivo = pasivo_corriente + pasivo_no_corriente
print("El total de activo corriente: {}".format(sum(activo_corriente)))
print("El total de activo no corriente: {}".format(sum(activo_no_corriente)))
print("El total de pasivo corriente: {}".format(sum(pasivo_corriente)))
print("El total de pasivo no corriente: {}".format(sum(pasivo_no_corriente)))
print("El total de pasivo: {}".format(sum(pasivo)))
print("El total de activo: {}".format(sum(activo)))