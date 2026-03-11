inventario = []

print("1. Agregar producto")
print("2. Mostrar inventario")
print("3. Calcular estadísticas")
print("4. Salir")

while True:
 opcion = (input("Seleccione una opción: "))

 if opcion == "1":
  def agregar():
   nombre = (input("Ingrese el nombre del producto: "))
   precio = int(input("ingrese el precio del producto: "))
   cantidad = int(input("ingrese la cantidad deseada: "))
   producto = {"nombre":nombre,"precio":precio,"cantidad":cantidad,}
   inventario.append(producto)

 elif opcion == "2":
    def mostrar():
     print(inventario)
     for i, producto in enumerate(inventario, start=1):
      print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
      if inventario == []:
       print("el inventario esta vacio")
        
 elif opcion == "3": 
     def calcular():
      valor_total = sum(i["cantidad"] * i["precio"] for i in inventario)
      print("valor del total de productos en el inventario:", valor_total)
      total_productos = len(inventario)
      print("cantidad total de productos registrados en el inventario:",total_productos)

 elif opcion == "4":
    print("Saliendo del programa")
    break
 else:
    print("el dato ingresado no es valido; ingrese nuevamente")