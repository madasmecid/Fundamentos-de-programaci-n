#FUNCIONES DE MENU

def mostrar_menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Visitas por especie")
    print("2. Busqueda por costo")
    print("3. Agregar mascota")
    print("4. Actualizar costo")
    print("5. Eliminar mascota")
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

#FUNCION DE BUSQUEDA

def buscar_mascota(codigo, atenciones):
    return codigo in atenciones

#FUNCION VALIDAR PALABRAS QUE NO ESTEN VACIAS

def validar_palabra(palabra):
    return len(palabra.strip()) > 0

#FUNCION 1 VISITA POR ESPECIE

def visitas_especie(especie, mascotas, atenciones):
    total_especie = 0
    for codigo, detalle in mascotas.items():
        if detalle[0].lower() == especie.lower():
            total_especie += atenciones[codigo][1]
    
    if total_especie > 0:
        print(f"Total de mascotas de la especie {especie}: {total_especie}")
    else:
        print(f"No hay mascotas de la especie {especie} ")









def sistema_central():
    # mascotas = {codigo:[especie,nombre,raza,sexo,edad], ...}

    mascotas = {
        'PER01':['Perro','Max','Pastor Aleman','Macho',5],
        'PER02':['Perro','Luna','Labrador','Hembra',3],
        'GAT01':['Gato','Michi','Siames','Macho',2],
        'GAT02':['Gato','Nina','Persa','Hembra',4],
        'AVE01':['Ave','Piolin','Canario','Macho',1],
        'AVE02':['Ave','Lola','Periquito','Hembra',2],
        'CON01':['Conejo','Copito','Mini Lop','Macho',3],
        'CON02':['Conejo','Nube','Holandes','Hembra',2]
    }

    atenciones = {
    'PER01':[25000,8],
    'PER02':[22000,4],
    'GAT01':[20000,6],
    'GAT02':[23000,3],
    'AVE01':[15000,7],
    'AVE02':[15000,2],
    'CON01':[18000,5],
    'CON02':[18000,4],
    'PER09':[28000,0]
}
    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            especie = input("Ingrese especie: ")
            if validar_palabra(especie):
                visitas_especie(especie, mascotas, atenciones)
            else:
                print("No puede dejar vacio. Intente nuevamente.")


        elif opcion == 6:
            print("Programa finalizado.")
            break












if __name__ == "__main__":
    sistema_central()