#==================================
#FUNCIONES DE MENÚ
#==================================

def mostrar_menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Stock por categoria ")
    print("2. Busqueda por precio")
    print("3. Agregar libro")
    print("4. Actualizar precio")
    print("5. Eliminar libro")
    print("6. Salir")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opcion valida!!")
        except ValueError:
            print("Debe seleccionar una opcion valida!!")

#==================================
#FUNCION BUSQUEDA
#==================================

def buscar_libro(codigo, inventario):
    return (codigo in inventario)


#==================================
#FUNCION STOCK POR CATEGORIA
#==================================

def stock_categoria(categoria, libros, inventario):
    total_categoria = 0
    for codigo, detalle in libros.items():
        if detalle[0].lower() == categoria.lower():
            total_categoria += inventario[codigo][1]

    if total_categoria > 0:
        print(f"El total de libros en la categoria {categoria.title()}: {total_categoria}")
    else:
        print("No existen libros en esa categoria")

#==================================
#FUNCION BUSQUEDA POR PRECIO
#==================================

def busqueda_precio(p_min, p_max, libros, inventario):
    libros_rango = []
    for codigo, detalle in libros.items():
        precio = inventario[codigo][0]
        stock = inventario[codigo][1]
        if (precio >= p_min and precio <= p_max) and stock > 0:
            libros_rango.append(f"{detalle[0]}--{codigo}")
    libros_rango.sort()
    return libros_rango

#==================================
#FUNCION AGREGAR LIBRO
#==================================

def agregar_libro(codigo, categoria, titulo, autor, idioma, estado, precio, cantidad, libros, inventario):
    if not buscar_libro(codigo, inventario):
        libros[codigo] = [categoria, titulo, autor, idioma, estado]
        inventario[codigo] = [precio, cantidad]
        return True
    return False

#==================================
#FUNCION ACTUALIZAR PRECIO
#==================================
def actualizar_precio(codigo, precio, libros, inventario):
    if buscar_libro(codigo, inventario):
        inventario[codigo][0] = precio
        return True
    return False

#==================================
#FUNCION ELIMINAR LIBRO
#==================================

def eliminar_libro(codigo, libros, inventario):
    if buscar_libro(codigo, inventario):
        del libros[codigo]
        del inventario[codigo]
        return True
    return False


#==================================
#FUNCION MAIN
#==================================


def central():
    libros = {  'NOV01':['Novela','1984','George Orwell','Español','Disponible'],
                'NOV02':['Novela','Dracula','Bram Stoker','Español','Disponible'],
                'CIE01':['Ciencia','Cosmos','Carl Sagan','Español','Disponible'],
                'CIE02':['Ciencia','Breves respuestas','Stephen Hawking','Español','Disponible'],
                'HIS01':['Historia','Sapiens','Yuval Harari','Español','Disponible'],
                'HIS02':['Historia','Roma','Indro Montanelli','Español','Disponible'],
                'INF01':['Informatica','Python Basico','Juan Perez','Español','Disponible'],
                'INF02':['Informatica','Algoritmos','Ana Soto','Español','Disponible']}
    

    inventario = {
        'NOV01':[10990,8],
        'NOV02':[9990,6],
        'CIE01':[14990,4],
        'CIE02':[16990,3],
        'HIS01':[18990,5],
        'HIS02':[15990,2],
        'INF01':[12990,7],
        'INF02':[13990,6],
        'NOV09':[21990,0]}
    
    while True:
        mostrar_menu()
        opcion = leer_opcion()


        if opcion == 1:

            categoria = input("Ingrese categoria: ").title()

            stock_categoria(categoria, libros, inventario)
        
        elif opcion == 2:
            while True:
                try:
                    minimo = int(input("Ingrese precio minimo: "))
                    maximo = int(input("Ingrese precio maximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            resultado = busqueda_precio(minimo, maximo, libros, inventario)

            if resultado:
                print(f"Encontrados en el rango: {resultado}")

            else:
                print("No hay libros en ese rango de precios.")

        elif opcion == 3:
            codigo = input("Ingrese codigo: ").upper()
            categoria = input("Ingrese categoria: ").title()
            titulo = input("Titulo: ").title()
            autor = input("Autor: ").title()
            idioma = input("Idioma: ").title()
            estado = input("Estado: ").title()
            while True:
                try:
                    precio = int(input("Ingrese el precio: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")

            while True:
                try:
                    cantidad = int(input("Ingrese cantidad: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")

            agregado = agregar_libro(codigo,categoria, titulo, autor, idioma, estado, precio, cantidad, libros, inventario)

            if agregado:
                print("Libro agregado!!")
            else:
                print("El libro ya existe!!")
        elif opcion == 4:
            codigo = input("Ingrese el codigo del precio a actualizar: ").upper()
            while True:
                try:
                    precio = int(input("Ingrese el nuevo precio: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            actualizado = actualizar_precio(codigo, precio, libros, inventario)

            if actualizado:
                print("Precio actualizado!!")

            else:
                print("El libro no existe!!")

        elif opcion == 5:
            codigo = input("Ingrese el codigo del libro a eliminar: ").upper()

            eliminado = eliminar_libro(codigo, libros, inventario)

            if eliminado:
                print("Libro eliminado!!")

            else:
                print("El libro no existe!!")



        elif opcion == 6:
            print("Programa finalizado.")
            break



if __name__ == "__main__":
    central()