pokemones = {
    'PIK025': ['Ash',   'Pikachu',   'Electrico', 'Kanto', 1, 'Alegre',    'Impactrueno'],
    'CHA006': ['Ash',   'Charizard', 'Fuego',     'Kanto', 1, 'Audaz',     'Lanzallamas'],
    'STA121': ['Misty', 'Starmie',   'Agua',      'Kanto', 1, 'Serena',    'Hidrobomba'],
    'ONI095': ['Brock', 'Onix',      'Roca',      'Kanto', 1, 'Firme',     'Lanzarrocas'],
    'EEV133': ['Gary',  'Eevee',     'Normal',    'Kanto', 1, 'Timida',    'Placaje'],
    'BLA257': ['May',   'Blaziken',  'Fuego',     'Hoenn', 3, 'Osada',     'Patada ignea'],
    'GAR282': ['May',   'Gardevoir', 'Psiquico',  'Hoenn', 3, 'Modesta',   'Psiquico'],
    'UMB197': ['Gary',  'Umbreon',   'Siniestro', 'Johto', 2, 'Cautelosa', 'Bola sombra'],
}

registro = {
    'PIK025': [1320, 3],
    'CHA006': [2890, 1],
    'STA121': [1450, 2],
    'ONI095': [980, 4],
    'EEV133': [640, 5],
    'BLA257': [2540, 1],
    'GAR282': [2310, 2],
    'UMB197': [1780, 1],
    'MAG129': [310, 0],
}


def mostar_menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Pokemon por entrenador")
    print("2. Busqueda por poder de combate")
    print("3. Actualizar poder de combate")
    print("4. Salir")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion >= 1 and opcion <= 4:
                return opcion
            else:
                print("Opción no valida!!")
        except ValueError:
            print("Opción no valida!!")

"""def esta_pokemon(codigo, pokemones):
    return (codigo in pokemones)"""

def pokemon_entrenador(entrenador_ingresado):
    
    cantidad = 0
    for codigo, entrenador in pokemones.items():
        if entrenador[0].lower() == entrenador_ingresado.lower():
            cantidad += registro[codigo][1]

    print(f"El total de pokemones del entrenador {entrenador_ingresado.title()} es: {cantidad}")

def busqueda_poder(p_min,p_max):
    lista_rangos = []
    

    for codigo, detalle in registro.items():
        poder = detalle[0]
        cantidad = detalle[1]
        if poder >= p_min and poder <= p_max and cantidad > 0:
            lista_rangos.append (f"{pokemones[codigo][0]}--{codigo}")

        lista_rangos.sort()

    if len(lista_rangos) > 0:
        print(f"Lo encontrado en el rango es: {lista_rangos}")
    else:
        print("No hay pokemon en ese rango de poder")


def actualizar_poder(codigo,nuevo_poder):
    if codigo in registro:
        registro[codigo][0] = nuevo_poder
        return True
    return False


def main ():

    while True:
        mostar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            entrenador = input("Ingrese el nombre del maestro pokemon:").lower()
            pokemon_entrenador(entrenador)

        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese poder minimo: "))
                    p_max = int(input("Ingrese poder maximo: "))
                    break
                except ValueError:
                    print("Valor debe ser numero entero!!")

            busqueda_poder(p_min,p_max)


        elif opcion == 3:
            codigo = input("Ingrese el codigo a actualizar: ")
        
            while True:
                try:
                    nuevo_poder = int(input("Ingrese el nuevo poder: "))
                    break
                except ValueError:
                    print("Ingrese un valor numerico entero!!")

            actualizar = actualizar_poder(codigo, nuevo_poder)

            if actualizar:
                print("poder actualizado!!")
            else:
                print("el pokemon no existe")


        elif opcion == 4:
            print("Programa finalizado.")
            break







if __name__ == "__main__":
    main()