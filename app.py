#1 creamos otro archivo donde guardaremos las funciones usadas en este programa. 
# Usamos import y el nombre del archivo para poder invocar las funciones en este codigo.
from servicios import agregar_producto, mostrar_inventario, buscar_producto, actualizar_producto,eliminar_producto,calcular_estadisticas
from archivos import cargar_csv,guardar_csv


#2 inicializamos las variables globales: inventario, los contadores de valor_total y cantidad_total,
# E inicializamos opcion = None para que nos funcione de manera correcta dentro del while.
opcion = 0
inventario = []
valor_total = 0
cantidad_total = 0 
nombre = None
precio = None
cantidad = None

#3 usamos el bucle while para que  nos aparezca el menu hasta que el usuario presione 4 para salir del programa.
while opcion != 9:
    print("-"*60)
    print("1. Agregar productos")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto ")
    print("6. Calcular estadisticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

#4 utilizamos try y except para controlar si hay un error, por ejemplo si el usuario ingresa un dato distinto a un numero.
# tambien usamos continue para que el programa vuelva al menu sin romperse.
    try:
       opcion = int(input("\n¿qué acción desea realizar? opciones (1-9): "))
    
# utilizamos condicionales para que el usuario solo pueda ingresar los numeros de cada opcion que les aparece.
# en el ultimo elif colocamos un mensaje que le indica al usuario que solo esta permitido ingresar entre 1 y 4.
       if opcion == 1:
          agregar_producto(inventario,nombre,precio,cantidad)
      
       elif opcion == 2:
           mostrar_inventario(inventario)

       elif opcion == 3:
           producto = buscar_producto(inventario)
           if  producto is None:
            print("producto no encontrado")
            input("presione ENTER para volver al menu: ")         
               
       elif opcion == 4:
         actualizar_producto(inventario)
         

       elif opcion == 5:
        eliminar_producto(inventario,nombre)
        nombre = input("Nombre del producto:")

       elif opcion == 6:
        calcular_estadisticas(inventario)
        
    
       elif opcion == 7:
          ruta = input("Nombre del producto:")
          guardar_csv(inventario,ruta)

    
       elif opcion == 8:
          cargar_csv(inventario,ruta)
          ruta = input("Nombre del archivo:")
          nuevos = cargar_csv(ruta)

          if nuevos:
             respuesta = input("Desea sobrescribir el inventario actual con los datos del archivo? si/no: ").lower
          if respuesta == "si":
           inventario = nuevos
          else:
           for nuevo in nuevos:
            existente = buscar_producto(inventario,nuevo["Nombre"])
            if existente:
              existente["cantidad"] += nuevo["cantidad"]
              existente["precio"] = nuevo["precio"]
            else:
              inventario.append(nuevo)

       elif opcion > 9 or opcion < 1:
        print("\nsolo es permitido colocar un número entre 1 y 4")
        input("presione ENTER para volver al menu: ")
  
    except ValueError:
     print("\nNO es valido colocar letras u otros simbolos, las opciones son entre 1 y 4")
     input("preione ENTER para volver al menu: ")
     

print("-"*60)
print("hasta luego!") 