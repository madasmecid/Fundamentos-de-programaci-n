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
    return(len(rut.strip())>= 9 and len(rut.strip()) <= 10)

def validar_nombre(nombre):
    return(len(nombre.strip()) >= 3)

def validar_puntos(puntos):
    return(puntos >= 0)

#======================================
#FUNCIÓN DE BUSQUEDA
#======================================

def buscar_rut (clientes_vip, rut_buscar):
    if rut_buscar in clientes_vip:
        return rut_buscar
    else:
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
        except ValueError:
            print("Dato ingresado no es valido.")

    clientes_vip[rut] = {"nombre": nombre, "puntos": puntos, "categoria": "Gold"}
    print("Cliente agregado exitosamente.")

#======================================
#FUNCIÓN MODIFICAR REGISTRO
#======================================

def modificar_cliente(clientes_vip):
    rut = input("Ingrese el rut del cliente a modificar: ")
    posicion = buscar_rut(clientes_vip, rut)
    if posicion != -1:
        cliente = clientes_vip[rut]
        print(f"Cliente encontrado: {cliente['nombre']}, Puntos: {cliente['puntos']}, Categoría: {cliente['categoria']}")
        
        while True:
            nombre = input("Ingrese nuevo nombre (dejar en blanco para no modificar): ")
            if nombre == "" or validar_nombre(nombre):
                break
            else:
                print("Nombre no es valido.")

        while True:
            puntos_input = input("Ingrese nuevos puntos (dejar en blanco para no modificar): ")
            if puntos_input == "":
                puntos = cliente['puntos']
                break
            try:
                puntos = int(puntos_input)
                if validar_puntos(puntos):
                    break
                else:
                    print("Dato ingresado no es valido.")
            except ValueError:
                print("Dato ingresado no es valido.")

        if nombre != "":
            cliente['nombre'] = nombre
        cliente['puntos'] = puntos

        print("Cliente modificado exitosamente.")

    else:
        print("Cliente no encontrado.")

#======================================
#FUNCIÓN ELIMINAR REGISTRO
#======================================

def eliminar_cliente(clientes_vip):
    rut = input("Ingrese el rut del cliente a eliminar: ")
    posicion = buscar_rut(clientes_vip, rut)
    if posicion != -1:
        del clientes_vip[rut]
        print("Cliente eliminado exitosamente.")
    else:
        print("Cliente no encontrado.")




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
            agregar_rut(clientes_vip)
        
        elif opcion == 2:
            rut_buscar = input("Ingrese el rut del cliente a buscar: ")
            indice = buscar_rut(clientes_vip, rut_buscar)
            if indice != -1:
                cliente = clientes_vip[rut_buscar]
                print(f"Cliente encontrado: {cliente['nombre']}, Puntos: {cliente['puntos']}, Categoría: {cliente['categoria']}")
            else:
                print("Cliente no encontrado.")
        
        elif opcion == 3:
            modificar_cliente(clientes_vip)
        
        elif opcion == 4:
            eliminar_cliente(clientes_vip)
        
        elif opcion == 5:
            print("Adios")
            break


if __name__ == "__main__":
    principal()