#====================================
#FUNCIONES DE MENU
#====================================

def mostrar_menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Stock por genero")
    print("2. Busqueda por precio")
    print("3. Agregar videojuego")
    print("4. Actualizar precio")
    print("5. Eliminar videojuego")
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





#=========================================================
#FUNCION PRINCIPAL MAIN
#=========================================================

def sistema_central():
    juegos = {
        'ACC01':['Accion','GTA V','PC','18+','Si'],
        'ACC02':['Accion','Red Dead Redemption 2','PS5','18+','No'],
        'DEP01':['Deportes','EA FC 26','PS5','Todo Publico','Si'],
        'DEP02':['Deportes','NBA 2K26','Xbox','Todo Publico','Si'],
        'ROL01':['Rol','Elden Ring','PC','16+','Si'],
        'ROL02':['Rol','Skyrim','PC','16+','No'],
        'EST01':['Estrategia','Age of Empires IV','PC','12+','Si'],
        'EST02':['Estrategia','Civilization VII','PC','12+','No']
        }
    
    inventario = {
        'ACC01':[39990,12],
        'ACC02':[45990,8],
        'DEP01':[54990,15],
        'DEP02':[49990,10],
        'ROL01':[42990,7],
        'ROL02':[19990,20],
        'EST01':[24990,18],
        'EST02':[29990,11],
        'ACC09':[59990,0]
        }
    
    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            pass


        elif opcion == 6:
            print("Programa finalizado.")
            break








if __name__ == "__main__":
    sistema_central()