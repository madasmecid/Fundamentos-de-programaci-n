#==============================
#FUNCIONES DE MENU PRINCIPAL
#==============================

def mostrar_menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Stock por tipo")
    print("2. Busqueda por precio")
    print("3. Agregar producto")
    print("4. Actualizar precio")
    print("5. Eliminar producto")
    print("6. Salir")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion del menú: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("opcion valida!!")
        except ValueError:
            print("opcion valida!!")

#==============================
#FUNCIÓN DE BUSQUEDA
#==============================

def existe_producto(codigo, inventario):
    return (codigo in inventario)

#==============================
#FUNCIÓN STOCK POR TIPO
#==============================

def stock_tipo(tipo,productos, inventario):
    cantidad_total = 0
    for codigo, detalle in productos.items():
        if detalle[0].lower() == tipo.lower():
            cantidad_total += inventario[codigo][1]
    if cantidad_total > 0:
        print(f"La cantidad total de {tipo} es: {cantidad_total}")
    else:
        print("No hay stock de ese tipo de producto.")

#==============================
#FUNCIÓN BUSQUEDA POR PRECIO
#==============================

def busqueda_precio(p_min,p_max,productos, inventario):
    lista_rango = []
    for codigo, detalle in productos.items():
        precio = inventario[codigo][0]
        stock = inventario[codigo][1]
        if (precio >= p_min and precio <= p_max) and stock > 0:
            lista_rango.append(f"{detalle[0]} -- {codigo}")

    lista_rango.sort()

    return lista_rango

#==============================
#FUNCIÓN AGREGAR PRODUCTO
#==============================

def agregar_producto(codigo, tipo, nombre, sabor, tamaño, vegano, precio, cantidad, productos, inventario):
    if not existe_producto(codigo, inventario):
        productos[codigo]=[tipo,nombre,sabor,tamaño,vegano]
        inventario[codigo]= [precio, cantidad]
        return True
    else:
        return False
    
#==============================
#FUNCIÓN ACTUALIZAR PRECIO
#==============================
def actualizar_precio(codigo, precio, inventario):
    if  existe_producto(codigo, inventario):
        for producto, detalle in inventario.items():
            if producto.lower() == codigo.lower():
                detalle[0] = precio
                return True
    return False

#==============================
#FUNCIÓN ELIMINAR PRODUCTO
#==============================

def eliminar_producto(codigo, productos, inventario):
    if existe_producto(codigo, inventario):
        del productos[codigo]
        del inventario[codigo]
        return True
    return False
            
#==============================
#FUNCIÓN PRINCIPAL
#==============================

def sistema_central():
    productos = {
    'TRT01': ['Torta',   'Selva Negra',    'Chocolate',   'Grande',     'No'],
    'TRT02': ['Torta',   'Tres Leches',    'Vainilla',    'Mediana',    'No'],
    'GAL01': ['Galleta', 'Chips de Choco', 'Chocolate',   'Individual', 'No'],
    'GAL02': ['Galleta', 'Avena y Pasas',  'Avena',       'Individual', 'Si'],
    'PAN01': ['Pan',     'Baguette',       'Natural',     'Grande',     'Si'],
    'PAN02': ['Pan',     'Croissant',      'Mantequilla', 'Individual', 'No'],
    'BEB01': ['Bebida',  'Cafe Latte',     'Cafe',        'Mediano',    'No'],
    'BEB02': ['Bebida',  'Jugo Natural',   'Naranja',     'Grande',     'Si'],
    }
    
    inventario = {
    'TRT01': [18990, 3],
    'TRT02': [15990, 2],
    'GAL01': [1290, 40],
    'GAL02': [1390, 25],
    'PAN01': [1990, 15],
    'PAN02': [1490, 30],
    'BEB01': [3490, 12],
    'BEB02': [2990, 8],
    'TRT09': [21990, 0],
    }

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            tipo = input("Ingrese el tipo de producto: ")

            stock_tipo(tipo, productos, inventario)

        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese el precio minimo: "))
                    p_max = int(input("Ingrese el precio maximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")

            resultado = busqueda_precio(p_min, p_max, productos, inventario)

            if resultado:
                print(f"Productos en su rango de precio: {resultado}")
            else:
                print("No hay productos en ese rango de precios.")

        elif opcion == 3:
            codigo = input("Ingrese codigo: ").upper()
            tipo = input("Tipo: ").title()
            nombre = input("Nombre: ").title()
            sabor = input("Sabor: ").title()
            tamaño = input("Tamaño: ").title()
            vegano = input("Es vegano?: ").title()
            while True:
                try:
                    precio = int(input("Ingrese precio: "))
                    break
                except ValueError:
                    print("Debe ser valor numerico entero")

            while True:
                try:
                    cantidad = int(input("Ingrese cantidad: "))
                    break
                except ValueError:
                    print("Debe ser valor numerico entero")

            agregar = agregar_producto(codigo,tipo,nombre,sabor,tamaño,vegano,precio,cantidad,productos,inventario)
            
            if agregar:
                print("Producto agregado!!")
            else:
                print("El producto ya existe!!")
                
        elif opcion == 4:
            codigo = input("-ingrese el codigo para actualizar precio: ").upper()
            while True:
                try:
                    precio = int(input("Ingrese el nuevo precio: "))
                    break
                except ValueError:
                    print("Debe ser un dato numerico")

            actualizado = actualizar_precio(codigo, precio, inventario)

            if actualizado:
                print("Precio actualizado!!")
            else:
                print("El producto no existe!!")

        elif opcion == 5:
            codigo = input("Ingrese el codigo del producto a eliminar: ").upper()
            eliminado = eliminar_producto(codigo,productos, inventario)

            if eliminado:
                print("Producto eliminado!!")
            else:
                print("El producto no existe!!")
            
        elif opcion == 6:
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    sistema_central()