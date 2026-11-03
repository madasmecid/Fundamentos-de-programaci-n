def contar_largas(lista):
    palabras_largas = 0
    for palabra in lista:
        if len(palabra) > 4:
            palabras_largas += 1

    return palabras_largas




def main ():

    herramientas = ["python", "java", "fedora", "git", "docker", "sql"]

    resultado = contar_largas(herramientas)

    print(f"La cantidad de palabras largas es: {resultado}")


if __name__ == "__main__":
    main()