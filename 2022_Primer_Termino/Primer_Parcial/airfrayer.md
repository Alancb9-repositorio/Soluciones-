# Airfryer

![airfyer](https://10mejores.top/wp-content/uploads/2019/01/Philips-Airfryer-XXL.jpg)

Para programar la Airfryer es necesario crear un programa en Python con las siguientes características:

Primero, deberá preguntar si ya colocó el alimento a calentar o no en la bandeja. En caso de aún no colocar el alimento en la bandeja, deberá mostrar "Debes colocar tu alimento en la bandeja" y *seguir preguntando*  mientras que no coloque el alimento. En caso de colocar el alimento en la bandeja, deberá continuar con el segundo paso.

En el segundo paso, mostrará todos los modos que ofrece el Airfryer. Cada modo tiene un nombre y el tiempo que toma.

modos = ['Descongelar - 30 minutos', 'Cocinar papas - 10 minutos' - 'Cocinar pescado - 5 minutos']

Luego, deberá ingresar el nombre válido de uno de los modos. Caso contrario, deberá volver a ingresar mientras que no sea un nombre válido.

Finalmente, de acuerdo con el modo seleccionado, el Airfryer mostrará cada minuto (1) un mensaje con el tiempo faltante. Hasta antes del minuto de finalización. Al finalizar, deberá mostrar el mensaje de '¡Listo!'.

Por ejemplo, asuma que el nombre del modo seleccionado fue 'Descongelar' 

Su programa mostrará algo como:

`'Faltan 30 minutos'
'Faltan 29 minutos' 
'Faltan 28 minutos'
...
'Faltan 2 minutos'
'¡Listo!'`