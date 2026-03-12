# Sistema Básico de Inventario en Python

## Descripcion

 Este proyecto es un programa sencillo en Python que permite registrar el nombre de un usuario, el precio de un producto y la cantidad comprada. El programa calcula automáticamente el costo total del producto multiplicando el precio por la cantidad.

Además, incluye validación de datos usando try y except para evitar errores cuando el usuario ingrese valores no numéricos.

## Funcionalidades
- Solicitar el nombre el usuario.
- Solicitar el precio del producto.
- Solicitar la cantidad del producto.
- Validar que el precio y la cantidad del producto sean datos numericos.
- Calcular el costo total segun las dos variables obtenidas.
- Mostrar los datos ingresados y el total en pantalla.

## Tecnologias utilizadas
- Python 3

## Cómo ejecutarlo

1. Asegúrate de tener Python 3 instalado en tu equipo.
2. Clona el repositorio:
```
   git clone <url-del-repositorio>
```
3. Ejecuta el programa con el siguiente comando:
```
   python inventario.py
```

## Usos
- Registrar ventas ingresando nombre del cliente, precio y cantidad.
- Calcular automáticamente el costo total de una compra.
- Validar que los datos ingresados sean numéricos, evitando errores en el registro.


## CODIGO inventario: registar nombre, precio del producto, cantidad del producto y calcular total de la venta.

```python

print("="*65)
print("REGISTRO DE VENTAS".center(65))
print("="*65)
#1 solicitamos los datos al usuario
nombre = input("ingrese su nombre: ")

print("-"*65)
#2 usamos try para validar que el usuario ingrese el dato valido y usamos while true para que lo pueda intentar nuevamente

while True:
   try:
    precio = float(input("ingrese el precio del producto: "))
    print("-"*65)
    cantidad = int(input("ingrese la cantidad: "))

#3 creamos una variable llamada costo_total para calcular el total entre precio y cantidad multiplicando precio por cantidad
    costo_total = precio * cantidad
    break
   except:
    print("el dato ingresado debe ser un valor numerico, intente nuevamente")

#4 por ultimo imprimo el resultado en pantalla con print y usamos la f para meter variables dentro de la cadena de texto
print("="*65)
print(f"Nombre: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")
print("="*65)

```

## Representacion en consola:
```
============================================================
                     REGISTRO DE VENTAS                     
============================================================
Ingrese su nombre: Juan
------------------------------------------------------------
Ingrese el precio del producto: 3000
Ingrese la cantidad: 4
============================================================
Nombre: Juan | Precio: 3000.0 | Cantidad: 4 | Total: 12000.0
============================================================
```

## Autores
### David Moran
### Juan Rangel
