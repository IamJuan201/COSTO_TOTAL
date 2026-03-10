# inventario : registar nombre,precio producto y calcular total
#1 primero solicitamos los datos al usuario
#2 usamos try para validar que el usuario ingrese el dato valido y usamos while true para que lo pueda intentar nuevamente
#3 creamos una variable llamada costo_total para calcular el total entre precio y cantidad multiplicando precio por cantidad
#4 por ultimo imprimo el resultado en pantalla
nombre = input("ingrese su nombre: ")
while True:     
   try:
    precio = int(input("ingrese el precio del producto: "))
    cantidad = int(input("ingrese la cantidad: "))
    costo_total = precio * cantidad
    break
   except:
    print("el dato ingresado debe ser un valor numerico, intente nuevamente")
print("nombre:", nombre)
print("precio:", precio)
print("cantidad:",cantidad)
print("total:",costo_total)