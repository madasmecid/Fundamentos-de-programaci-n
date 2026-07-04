#======================================
#FUNCIONES MENU
#======================================
def mostrar_menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Pokemon por entrenador")
    print("2. Busqueda por poder de combate")
    print("3. Actualizar poder de combate")
    print("4. Salir")

def opcion_menu():
    while True:
        opcion = input("Ingrese una opción: ")
        if opcion in ['1','2','3','4']:
            return int (opcion)
        print("Opcion no valida. Intente nuevamente.")

#======================================
#FUNCION POKEMON POR ENTRENADOR
#======================================

def pokemones_entrenador(pokemones, registro, maestro_user):
    pokemones_total = 0
    for codigo, detalle in pokemones.items():
        maestro = detalle[0]
        if maestro.lower() == maestro_user.lower():
            pokemones_total += registro[codigo][1]
    return pokemones_total

#======================================
#FUNCION BUSCAR POR PODER DE COMBATE
#======================================

def buscar_poder(pokemones, registro, p_min, p_max):
    pokemones_rango = []
    for codigo, detalle in registro.items():
        if codigo in pokemones:
            entrenador = pokemones[codigo][0]
            poder = registro[codigo][0]
            if (poder >= p_min and poder <= p_max) and poder > 0:
                pokemones_rango.append(f"{entrenador}--{codigo}")
    pokemones_rango.sort()
    return pokemones_rango


#======================================
#FUNCION ACTUALIZAR PODER DE COMBATE
#======================================

def actualizar_poder(registro, codigo, poder):
    if codigo in registro:
        registro[codigo][0] = poder
        return True






def sistema_central():
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
    
    while True:
        mostrar_menu()
        opcion = opcion_menu()

        if opcion == 1:
            entrenador = input("Ingrese el entrenador: ")
            total_pokemones = pokemones_entrenador(pokemones, registro, entrenador)

            if pokemones:
                print(f"EL total de pokemones del entrenador {entrenador.title()} es {total_pokemones}")
            else:
                print("No se encontro entrenador.")

        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese poder minimo: "))
                    p_max = int(input("Ingrese poder maximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
                    continue


            rango_poder = buscar_poder(pokemones, registro, p_min, p_max)

            if rango_poder:
                print(f" los encontrados fueron: {rango_poder}")

            else:
                print("No se encontraron en ese rango")


        elif opcion == 3:
            codigo = input("Ingrese el codigo del pokemon que quiere modificar: ")
            poder = int(input("Ingrese el poder nuevo: "))

            pokemon_actualizado = actualizar_poder(registro, codigo, poder)

            if pokemon_actualizado:
                print("Se actualizo el poder de combate.")
            else:
                print("No se actualizo nada.")

        elif opcion == 4:
            print("Adios")
            break


if __name__ == "__main__":
    sistema_central()