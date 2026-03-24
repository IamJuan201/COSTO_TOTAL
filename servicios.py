opcion = None
inventario = []
valor_total = 0
unidad_total = 0
nombre = None
precio = None
cantidad = None


def agregar_producto(inventario,nombre,precio,cantidad):
        
        print("-"*60)
        productos = int(input("\ningrese la cantidad de productos que desea: "))
        
        for i in range(productos):
            nombre = input("ingrese el nombre del producto: ")
            precio = float(input("ingrese el precio del producto: "))
            cantidad = int(input("ingrese la cantidad del producto: "))
            
            producto = {"Nombre": nombre, "precio": precio, "cantidad": cantidad}
            inventario.append(producto)

def mostrar_inventario(inventario):
        if len(inventario) == 0:
            print("el inventario está vacío")
        else:
            for producto in inventario:
                print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def buscar_producto(inventario,nombre):
    for producto in inventario:
         if producto ["nombre"].lower() == nombre.lower().strip():
              return producto
         return None

def actualizar_producto(inventario,nombre,nuevo_precio=None,nueva_cantidad=None):
    producto = buscar_producto(inventario,nombre)
    
    if not producto:
         print(f"El producto ")
    
    try:
         nuevo_precio = input("nuevo precio (ENTER para omitir):")
         nueva_cantidad = input("nueva cantidad(ENTER para omitir):")

         if nuevo_precio:
              producto["precio unitario"] = float(nuevo_precio)
         if nueva_cantidad:
              producto["cantidad"] = int(nueva_cantidad)
         
         print("producto actualizado")
    except:
         print("El precio y la cantidad deben ser datos numericos")

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