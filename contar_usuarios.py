def contar_usuarios(lista):
    conteo = {}
    for nombre in lista:
        nombre_limpio = nombre.strip().upper()

        if nombre_limpio in conteo:
            conteo[nombre_limpio] += 1
        else:
            conteo[nombre_limpio] = 1

    return conteo


def main():

    usuarios_malos= ["  juan ", "maria ", " PEDRO", "  juan", "  MARIA  ", "diego "]

    resultado = contar_usuarios(usuarios_malos)

    print(resultado)



if __name__ == "__main__":
    main()