#funciones
def productoMayorVentaTotal(C,PU,CN):
  monto_ventaTotal= []
  for i in range(len(PU)):#puede ser cualquier lista. (0,1,2,3,4) i = 0
    precio_unitario=PU[i]
    total_vendido=CN[i]
    multiplicar= precio_unitario*total_vendido
    monto_ventaTotal.append(multiplicar)
  maximo= max(monto_ventaTotal)
  indice_maximo= monto_ventaTotal.index(maximo)
  codigo_maximo=C[indice_maximo]
  return codigo_maximo




#Programa principal
codigos = ["cod1","cod2","cod3","cod4","cod5"]
precios_unitarios= [1.5, 2.5, 3.5, 1.2, 3.2]
total_vendidos = [100, 22, 35, 70, 80]
categorias = ["yogurt","burger","yogurt","burger","burger"]
cod_maximo = productoMayorVentaTotal(codigos,precios_unitarios,total_vendidos)
print(cod_maximo)









    

    