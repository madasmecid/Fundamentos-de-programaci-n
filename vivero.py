#=======================================
#FUNCIONES PRINCIPALES
#=======================================
def mostrar_menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Stock por tipo")
    print("2. Busqueda por precio")
    print("3. Agregar planta")
    print("4. Actualizar precio")
    print("5. Eliminar planta")
    print("6. Salir")

def opcion_menu ():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Opcion no valida!!")
        except ValueError:
            print("Opcion no valida!!")

#=======================================
#FUNCIÓN DE BUSQUEDA
#=======================================
"""Esta funcion lo que hace es ver si el codigo ingresado por el usuario 
existe en el diccionario, no es necesario usar cicos, los argumentos son codigo
ingresado por el usuario y la lista plantas, y la condicional
si codigo esta en plantas retorna true sino retorna false."""
def planta_existe(codigo, plantas):
    if codigo in plantas:
        return True
    return False
    


#=======================================
#FUNCIÓN STOCK POR TIPO
#=======================================
"""Esta funcion suma y muestra el stock total de un tipo de planta,
como argumento resive plantas, inventario y tipo ingresado por el usuario,
inicia una variable acumuladora de total stock, iniciamos un ciclo con dos
variables, la primera guarda la llave y la segunda el diccionario, 
preguntamos si detalle en el indice 0 que es el tipo es igual al ingresado por el usuario,
si es asi sumamos desde el diccionario inventario la llave codigo en el indice 1
que es el stock actual y al final retornamos el total_tipo sumado por todos los ciclos."""
def stock_tipo(plantas, inventario, tipo):
    total_tipo = 0
    for codigo, detalle in plantas.items():
        if detalle[0].lower() == tipo.lower():
            total_tipo += inventario[codigo][1]

    if total_tipo > 0:
        print(f"EL total de stock de este tipo es: {total_tipo}")
    else:
        print("No hay stock en ese tipo")


#=======================================
#FUNCIÓN BUSQUEDA POR PRECIO
#=======================================
"""En esta funcion buscamos plantas que este en el rango de precio
ingresado por el usuario (minimo, maximo) mas los argumentos plantas y el inventario,
iniciamos una lista que guardara cada planta con su tipo y codigo en esa lista
ordenada alfabeticamente con .sort(). en la variable stock guardamos lo que esta
en inventario clave codigo que dio el ciclo y en el indice 1 que contiene el stock
de la planta, y en precio lo mismo pero el indice 0 que contiene el precio
de la planta, luego preguntamos si precio esta en el rango minimo y maximo y
ademas que sea el stock mayor a 0, si todo se cumple guardamos en la lista 
iniada al principio con .append(). la ordenamos alfabeticamente con sort()
y retornamos la lista"""
def busqueda_precio (minimo, maximo, plantas, inventario):
    lista_total = []
    for codigo, detalle in plantas.items():
        stock  = inventario[codigo][1]
        precio = inventario[codigo][0]
        if (precio >= minimo and precio <= maximo) and stock > 0:
            lista_total.append(f"{detalle[0]}--{codigo}")

    lista_total.sort()

    return lista_total

#=======================================
#FUNCIÓN AGREGAR
#=======================================
"""Los argumentos para esta función son todas las carecteristica de una nueva
planta mas el precio y cantidad (stock), y los diccionarios plantas y inventario,
para que se guarde y no se sobre escriba crearemos una variable nueva_planta,
esta tomara el valor de el largo del diccionario mas 1, luego agregamos al diccionario
plantas y luego inventario y finalmente retornamos True"""
def agregar_planta(codigo, tipo, nombre, color, luz, riego, precio, cantidad, plantas,  inventario):
    
     
     plantas[codigo] = [tipo, nombre,color,luz,riego]
     inventario [codigo] = [precio, cantidad]
     return True
    
#=======================================
#FUNCIÓN ACTUALIZAR PRECIO
#=======================================
def actualizar_precio(codigo, precio, plantas, inventario):
    if planta_existe(codigo, plantas):
        inventario[codigo][0] = precio
        return True
    
    return False

#=======================================
#FUNCIÓN ELIMINAR PLANTA
#=======================================
"""Esta funcion recibe como argumento el codigo, diccionarios plantas e inventario,
reutiliza la funcion planta existe(busqueda) si esta entrega True entra al diccionario
plantas en la clave codigo que coincide con la que ingreso el usario y elimina con "deñl"
hce lo mismo en inventario y retorna True, sino retorna False"""
def eliminar_planta(codigo, plantas, inventario):
    if planta_existe(codigo,plantas):
        del plantas[codigo]
        del inventario[codigo]
        return True
    return False

#=======================================
#FUNCIONES MAIN
#=======================================

def principal ():
    
    plantas = { 'SUC01': ['Suculenta', 'Echeveria', 'Verde', 'Alta', 'Bajo'], 
                'SUC02': ['Suculenta', 'Jade', 'Verde', 'Alta', 'Bajo'], 
                'INT01': ['Interior', 'Pothos', 'Verde', 'Media', 'Medio'], 
                'INT02': ['Interior', 'Monstera', 'Verde', 'Media', 'Medio'], 
                'EXT01': ['Exterior', 'Lavanda', 'Morado', 'Alta', 'Bajo'], 
                'EXT02': ['Exterior', 'Rosal', 'Rojo', 'Alta', 'Alto'], 
                'CAC01': ['Cactus', 'Cactus Bola', 'Verde', 'Alta', 'Bajo'], 
                'FLO01': ['Flor', 'Orquidea', 'Blanco', 'Media', 'Medio'],
                  }
    
    inventario = { 'SUC01': [3990, 20], 
                  'SUC02': [4490, 15],
                  'INT01': [6990, 10], 
                  'INT02': [12990, 4], 
                  'EXT01': [5490, 8], 
                  'EXT02': [7990, 6], 
                  'CAC01': [3490, 25], 
                  'FLO01': [14990, 3], 
                  'FLO09': [19990, 0], 
                  }
    
    while True:
        mostrar_menu()
        opcion = opcion_menu()


        if opcion == 1:
            tipo = input("ingrese tipo de planta: ")
            stock_tipo(plantas, inventario, tipo)
            

        elif opcion == 2:
            while True:
                try:
                    minimo = int(input("Ingrese precio minimo: "))
                    break
                except ValueError:
                    print("Debe ser valor numerico")
            
            while True:
                try:
                    maximo = int(input("Ingrese precio maximo: "))
                    break
                except ValueError:
                    print("Debe ser valor numerico")

            total = busqueda_precio(minimo, maximo, plantas, inventario)

            if total:
                print(f"Los encontrados en el rango son: {total}")
            else:
                print("NO se encontro nada en ese rango.")
        
        elif opcion == 3:
            codigo = input("Ingrese codigo: ").upper()
            if planta_existe(codigo, plantas):
                print("Planta ya existe!")
                continue
            
            tipo = input("Tipo: ")
            nombre = input("Nombre: ")
            color = input("Color: ")
            luz = input("Luz: ")
            riego = input("Riego: ")
            while True:
                try:
                    precio = int(input("Precio: "))
                    break
                except ValueError:
                    print("Ingrese un valor numerico entero!")
            while True:
                try:
                    cantidad = int(input("Cantidad: "))
                    break
                except ValueError:
                    print("Ingrese un valor numerico entero!")

            nueva_planta = agregar_planta(codigo, tipo, nombre, color, luz, riego, precio, cantidad, plantas, inventario)

            if nueva_planta:
                print("Se agrego correctamente")



        elif opcion == 4:
            codigo = input("Ingrese el codigo: ").upper()
            while True:
                try:
                    precio = int(input("Ingrese el precio nuevo: "))
                    break
                except ValueError:
                    print("Valor debe ser numerico")
            nuevo_precio = actualizar_precio(codigo, precio, plantas, inventario)
            if nuevo_precio:
                print("Precio actualizado")
            else:
                print("No se actualizo")

        elif opcion == 5:
            codigo = input("Ingrese el codigo de la planta a eliminar:")

            eliminar = eliminar_planta(codigo, plantas, inventario)

            if eliminar:
                print("Planta eliminada")
            else:
                print("Planta no existe!")

        elif opcion == 6:
            print("Programa finalizado.")
            break
if __name__ == "__main__":
    principal()