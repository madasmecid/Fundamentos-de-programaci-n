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
        print(f"Total de visitas de la especie {especie}: {total_especie}")
    else:
        print(f"No hay mascotas de la especie {especie} ")
        
#FUNCION 2 BUSQUEDA POR COSTO

def busqueda_costo(minimo, maximo, mascotas, atenciones):
    lista_encontrados = []
    for codigo, detalle in mascotas.items():
        costo = atenciones[codigo][0]
        visitas = atenciones[codigo][1]
        if (costo >= minimo and costo <= maximo) and visitas > 0:
            lista_encontrados.append(f"{detalle[0]}--{codigo}")

    lista_encontrados.sort()

    return lista_encontrados

#FUNCION 3 AGREGAR MASCOTA

def agregar_mascota(codigo, especie, nombre, raza, sexo, edad, costo, cantidad_visitas, mascotas, atenciones):
    if not buscar_mascota(codigo, atenciones):
        mascotas[codigo]= [especie, nombre, raza, sexo, edad]
        atenciones[codigo]=[costo, cantidad_visitas]
        return True
    return False

#FUNCION 4 ACTUALIZAR COSTO

def actualizar_costo(codigo, costo, mascotas, atenciones):
    if buscar_mascota(codigo, atenciones):
        atenciones[codigo][0] = costo
        return True
    return False

#FUNCION 5 ELIMINAR MASCOTA

def eliminar_mascota(codigo, mascotas, atenciones):
    if buscar_mascota(codigo, atenciones):
        del mascotas[codigo]
        del atenciones[codigo]
        return True
    return False






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
            while True:
                especie = input("Ingrese especie: ")
                if validar_palabra(especie):
                    visitas_especie(especie, mascotas, atenciones)
                    break
                else:
                    print("No puede dejar vacio. Intente nuevamente.")

        elif opcion == 2:
            while True:
                try:
                    minimo = int(input("Ingrese el valor minimo: "))
                    maximo = int(input("Ingrese el valor maximo: "))
                    if minimo < maximo:
                        break
                    else:
                        print("El minimo debe ser menor que el maximo.")
                except ValueError:
                    print("Debe ingresar valores enteros!!")

            encontrados = busqueda_costo(minimo, maximo, mascotas, atenciones)

            if encontrados:
                print(f"Los encontrados fueron: {encontrados}")
            else:
                print("No hay mascotas en ese rango de costos.")

        elif opcion == 3:
            while True:
                codigo = input("Ingrese codigo: ").upper()
                if validar_palabra(codigo):
                    break
                else:
                    print("EL campo no puede quedar vacio")
            if buscar_mascota(codigo, atenciones):
                print("La mascota ya existe!!")
            else:
                while True:
                    especie = input("Ingrese especie: ").title()
                    if validar_palabra(especie):
                        break
                    else:
                        print("EL campo no puede quedar vacio")
                while True:
                    nombre = input("Ingrese nombre: ").title()
                    if validar_palabra(nombre):
                        break
                    else:
                        print("EL campo no puede quedar vacio")
                while True:
                    raza = input("Ingrese raza: ").title()
                    if validar_palabra(raza):
                        break
                    else:
                        print("EL campo no puede quedar vacio")
                while True:
                    sexo = input("ingrese sexo: ").title()
                    if validar_palabra(sexo):
                        break
                    else:
                        print("EL campo no puede quedar vacio")
                while True:
                    try:
                        edad = int(input("Ingrese edad:  "))
                        break
                    except ValueError:
                        print("Ingrese valor númerico entero!!")
                while True:
                    try:
                        costo = int(input("Ingrese costo: "))
                        break
                    except ValueError:
                        print("Ingrese valor numerico entero!!")
                while True:
                    try:
                        cantidad_visitas = int(input("Ingrese cantidad: "))
                        break
                    except ValueError:
                        print("Ingrese valor numerico entero!!")

                agregado = agregar_mascota(codigo, especie, nombre, raza, sexo, edad, costo, cantidad_visitas, mascotas, atenciones)
                if agregado:
                    print("Mascota agregada!!")

        elif opcion == 4:
            while True:
                codigo = input("Ingrese codigo: ").upper()
                if validar_palabra(codigo):
                    break
                else:
                    print("El campo no puede quedar vacio. Intente nuevamente.")
            if not buscar_mascota(codigo, atenciones):
                print("La mascota no existe!!")
            else:


                while True:
                    try:
                        costo= int(input("Ingrese el nuevo costo: "))
                        break
                    except ValueError:
                        print("Ingrese un valor numerico entero!!")

                actualizado = actualizar_costo(codigo, costo, mascotas, atenciones)

                if actualizado:
                    print("Costo actualizado!!")
                
        elif opcion == 5:
            while True:
                codigo = input("Ingrese el codigo de la mascota que quiere eliminar: ").upper()
                if validar_palabra(codigo):
                    break
                else:
                    print("El campo no puede quedar vacio. Intente nuevamente.")

            eliminado = eliminar_mascota(codigo, mascotas, atenciones)

            if eliminado:
                print("Mascota eliminada!!")
            else:
                print("La mascota no existe!!")


        elif opcion == 6:
            print("Programa finalizado.")
            break












if __name__ == "__main__":
    sistema_central()