#======================================
#FUNCIONES DE MENU Y SELECCION OPCIONES
#======================================

def mostrar_menu():
    print("======MENÚ PRINCIPAL=====")
    print("1. Agregar Cliente VIP")
    print("2. Buscar Cliente VIP")
    print("3. Modificar Datos de Cliente")
    print("4. Eliminar Cliente VIP")
    print("5. Salir")

def opcion_menu():
    while True:
        opcion = input("Ingrese una opción del menú: ")
        if opcion in ['1','2','3','4','5']:
            return int(opcion)
        print("Opción no válida. Intente nuevamente.")

#======================================
#FUNCIONES DE VÁLIDACIÓN
#======================================

def validar_rut(rut):
    return(len(rut.strip()>= 9 and len(rut.strip() <= 10)))

def validar_nombre(nombre):
    return(len(nombre.strip() >= 3))

def validar_puntos(puntos):
    return(puntos >= 0)

#======================================
#FUNCIÓN DE BUSQUEDA
#======================================

def buscar_rut (clientes_vip, rut_buscar):
    for i in range (len(clientes_vip)):
        if clientes_vip[i] == rut_buscar:
            return i
    return -1

#======================================
#FUNCIÓN DE AGREGAR
#======================================

def agregar_rut(clientes_vip):
    while True:
        rut = input("Ingrese el rut: ")
        if validar_rut(rut):
            break
        else:
            print("Rut no es valido")

    while True:
        nombre = input("Ingrese nombre: ")
        if validar_nombre(nombre):
            break
        else:
            print("Nombre no es valido.")

    while True:
        try:
            puntos = int(input("ingrese puntos: "))
            if validar_puntos(puntos):
                break
            else:
                print("Dato ingresado no es valido.")

    #PENDIENTE AGREGAR








#======================================
#FUNCIÓN PRINCIPAL
#======================================

def principal ():
    clientes_vip = {
    "12345678-9": {"nombre": "Ana Gómez", "puntos": 1500, "categoria": "Platinum"},
    "18765432-1": {"nombre": "Carlos Soto", "puntos": 450, "categoria": "Gold"}
}
    
    while True:
        mostrar_menu()
        opcion = opcion_menu()

        if opcion == 1:
            pass
        
        elif opcion == 2:
            pass
        
        elif opcion == 3:
            pass
        
        elif opcion == 4:
            pass
        
        elif opcion == 5:
            print("Adios")
            break