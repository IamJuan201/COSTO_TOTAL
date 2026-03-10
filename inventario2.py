menu = []

print("1. Agregar producto")
print("2. Mostrar inventario")
print("3. Calcular estadísticas")
print("4. Salir")

while True:
 opcion = (input("Seleccione una opción: "))

 if opcion == "1":
    producto = input("Ingrese el nombre del producto: ")
    menu.append(producto)

 elif opcion == "2":
    print(menu)

 elif opcion == "3":
    print("Cantidad de productos:", len(menu))

 elif opcion == "4":
    print("Saliendo del programa")
    break
 else:
    print("el dato ingresado no es valido; ingrese nuevamente")