def mostrar_menu():
    
    print("*** MENU PRINCIPAL ***")
    print("1. Stock por categoria")
    print("2. Busqueda por precio")
    print("3. Agregar producto")
    print("4. Actualizar precio")
    print("5. Eliminar producto")
    print("6. Valor total del inventario")
    print("7. Salir")

def opcion_menu():
    while True:
        try:
            opcion = int(input("Ingrese la opcion: "))
            if opcion >= 1 and opcion <= 7:
                return opcion
            else:
                print("Opcion no valida")
        except ValueError:
            print("Opcion debe ser un numero entero.")

def existe_producto(codigo, inventario):
    return codigo in inventario


def stock_categoria (productos, inventario, categoria_buscar):
    total_stock = 0

    for codigo, detalle in productos.items():
        if detalle [0].lower()== categoria_buscar.lower():
            total_stock += inventario[codigo][1]

    return total_stock

def busqueda_precio (minimo, maximo, productos, inventario):
    lista_resultado = []
    for codigo, stock in inventario.items():
        precio = stock[0]
        cantidad = stock [1]

        if (precio >= minimo and precio <= maximo) and cantidad > 0:

            categoria = productos[codigo][0]

            lista_resultado.append(f"{categoria}--{codigo}")

    lista_resultado.sort()

    return lista_resultado

def agregar_producto(codigo, categoria, nombre, marca, estado, garantia, precio, cantidad, productos, inventario):
    if existe_producto(codigo, inventario):
        return False
    
    productos[codigo]=[
        categoria,
        nombre,
        marca,
        estado,
        garantia
    ]

    inventario[codigo] = [
        precio,
        cantidad
    ]

    return True

def actualizar_precio (codigo, nuevo_precio, inventario):
    if not existe_producto(codigo, inventario):
        return False
    
    inventario[codigo][0] = nuevo_precio

    return True

def eliminar_producto (codigo, productos, inventario):
    if not existe_producto(codigo, inventario):
        return False
    del productos[codigo]
    del inventario[codigo]

    return True





def principal ():
   

        productos = {
            "CEL01": ["Celular", "Galaxy A15", "Samsung", "Nuevo", "Si"],
            "CEL02": ["Celular", "iPhone 11", "Apple", "Usado", "No"],
            "COM01": ["Computador", "Notebook IdeaPad", "Lenovo", "Nuevo", "Si"],
            "COM02": ["Computador", "MacBook Air", "Apple", "Usado", "No"],
            "AUD01": ["Audio", "Audifonos Bluetooth", "Sony", "Nuevo", "Si"],
            "AUD02": ["Audio", "Parlante Go", "JBL", "Nuevo", "Si"],
            "ACC01": ["Accesorio", "Mouse Inalambrico", "Logitech", "Nuevo", "Si"],
            "ACC02": ["Accesorio", "Teclado Gamer", "Redragon", "Usado", "No"]
        }

       

        inventario = {
            "CEL01": [159990, 8],
            "CEL02": [299990, 3],
            "COM01": [449990, 5],
            "COM02": [699990, 2],
            "AUD01": [39990, 15],
            "AUD02": [29990, 10],
            "ACC01": [12990, 20],
            "ACC02": [24990, 0]
        }

        while True:
            mostrar_menu()
            opcion = opcion_menu()

            if opcion == 1:
                producto = input("Ingrese el producto que busca: ")
                posicion = stock_categoria(productos, inventario, producto)
                
                print(posicion)
            elif opcion == 2:
                while True:
                    try:
                        precio_min = int(input("Ingrese el precio minimo: "))
                        precio_max = int(input("Ingrese el precio maximo: "))
                        break
                    except ValueError:
                        print("Debe ingresar valores enteros")

                lista = busqueda_precio(precio_min, precio_max, productos, inventario)

                if len(lista) > 0:
                    print(lista)
                else:
                    print("No hay productos en ese rango")

            elif opcion == 3:
                codigo = input("Ingrese codigo: ")
                cateogria = input("Ingrese categoria: ")
                nombre = input("Ingrese nombre: ")
                marca = input("Ingrese marca: ")
                estado = input("Ingrese estado: ")
                garantia = input("Ingrese garantia: ")

                while True:
                    try:
                        precio= int(input("Ingrese preecio"))
                        break
                    except ValueError:
                        print("Valor debe ser numerico")

                while True:
                    try:
                        cantidad = int(input("Ingrese cantidad: "))
                        break
                    except ValueError:
                        print("Ingrese un valor numerico")

                agregado = agregar_producto(codigo, cateogria, nombre, marca, estado, garantia, precio, cantidad, productos, inventario)


                if agregado:
                    print("producto agregado")
                else:
                    print("El producto ya existe")                


    


if __name__ == "__main__":
    principal()