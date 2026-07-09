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

            categoria = input("Ingrese categoria: ")

            stock_categoria(categoria, libros, inventario)



        if opcion == 6:
            print("Programa finalizado.")
            break




if __name__ == "__main__":
    central()