opcion = None
inventario = []
valor_total = 0
unidad_total = 0
nombre = None


def agregar_producto(inventario,nombre,precio,cantidad):
        
        print("-"*60)
        productos = int(input("\ningrese la cantidad de productos que desea: "))
        
        for i in range(productos):
            nombre = input("ingrese el nombre del producto: ")
            precio = float(input("ingrese el precio del producto: "))
            cantidad = int(input("ingrese la cantidad del producto: "))
            
            producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
            inventario.append(producto)

def mostrar_inventario(inventario):
        if len(inventario) == 0:
            print("el inventario está vacío")
            input("presiona ENTER para volver al menu:")
        else:
            for producto in inventario:
                print(f"Nombre: {producto["nombre"]}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
            input("presione ENTER para volver al menu:")

def buscar_producto(inventario):
    nombre = input("Nombre del producto: ")
    for producto in inventario:
         if producto["nombre"].lower() == nombre.lower().strip():
          return producto
    return None

def actualizar_producto(inventario):
    # Dejamos que buscar_producto haga el trabajo de pedir el nombre y encontrarlo
    producto = buscar_producto(inventario)
    
    if not producto:
        print("Producto no encontrado.")
        # Aquí lo colocas para que el usuario lea el error antes de que el menú se imprima otra vez
        input("Presione ENTER para volver al menú...") 
        return

    try:
        n_precio = input("Nuevo precio (ENTER para omitir): ")
        n_cantidad = input("Nueva cantidad (ENTER para omitir): ")

        if n_precio:
            producto["precio"] = float(n_precio)
        if n_cantidad:
            producto["cantidad"] = int(n_cantidad)
         
        print("¡Producto actualizado con éxito!")
        input("Presione ENTER para continuar...") # También puedes ponerlo al final del éxito

    except ValueError:
        print("Error: El precio y la cantidad deben ser datos numéricos.")
        input("Presione ENTER para volver al menú...") # Y aquí para errores de escritura

def eliminar_producto(inventario,nombre):
      producto = buscar_producto(inventario,nombre)

      if not producto:
        print(f"El '{nombre}' no se encontro registrado")
        return
        
      inventario.remove(producto)
      print(f"El '{nombre}' fue eliminado")

def calcular_estadisticas(inventario):
        if not inventario:
            print("el inventario está vacío, debes agregar productos")
        
            valor_total = 0
            unidad_total = 0
            
            for producto in inventario:
                valor_total += producto["precio"] * producto["precio unitario"]
                unidad_total += producto["cantidad"]

                producto_mas_caro = inventario[0]
                producto_mayor_stock = inventario[0]

            for producto in inventario:
                 if producto["precio unitario"] > producto_mas_caro["precio unitario"]:
                      producto_mas_caro = producto
                 if producto["cantidad"] > producto_mayor_stock["cantidad"]:
                      producto_mayor_stock = producto
                

            print(f"cantidad total de unidades registradas: {unidad_total}")
            print(f"valor total del inventario: {valor_total}")
            print(f"Producto mas caro: {producto_mas_caro}")
            print(f"Producto con mayor stock: {producto_mayor_stock}")