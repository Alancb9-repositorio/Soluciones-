El local de comidas rápidas “Yogurt DonBolaños” desea mejorar el servicio brindado a sus clientes con el fin de aumentar sus ventas y relaciones públicas en este nuevo año. Como encargado del sistema se le otorgan varias listas con determinada información de la empresa. A continuación, se detallan los datos que almacena cada lista:

C: Los códigos de los productos vendidos en el local.

PU: El precio unitario de cada producto.

CN: La cantidad total de cada producto vendido.

CT: La categoría a la que pertenece cada producto.

Las listas son paralelas entre sí.

Implementar la función productoMayorVentaTotal(C,PU,CN) que recibe las listas C,PU,CN. La función entrega como resultado el código del producto que mayor monto de venta total ha generado. El monto de venta total se calcula multiplicando el precio unitario por las unidades vendidas de cada producto.

Implementar la función calcularVentaTotal(codigo,C,PU,CN) que recibe un código de producto y las listas C,PU,CN. La función entrega como resultado el monto total de venta del código de producto que recibe como argumento la función. El monto de venta total se calcula multiplicando el precio unitario por las unidades vendidas de cada producto.

Implementar la función calcularVentaTotalProductos(codigos,C,PU,CN) que recibe una lista de códigos de productos cualquiera y las listas C,PU,CN. La función entrega como resultado el monto total de venta acumulado de todos los códigos que recibe la función.

Implementar la función productosMayorVenta(limite,C,PU,CN) que recibe un valor float que representa un límite inferior. La función entrega como resultado la cantidad de productos cuyo monto total de venta sea superior al límite que recibe la función.

Implementar la función cantidadVendidas(CN,minimo,maximo) que recibe la lista CN y dos valores enteros que representan un valor mínimo y máximo. La función entrega como resultado la suma de todas las cantidades totales de productos que se encuentran dentro del rango de mínimo y máximo.

Implementar la función top(C,PU,CN) que recibe las listas C,PU,CN. La función entrega como resultado el top 3 de los códigos que mayor venta total generaron.

Implementar la función categoriaMasVendida(CT,PU,CN) que recibe las listas CT,PU,CN. La función entrega como resultado la categoría que mayor monto total de venta ha generado.
