def clasificar_equipos(lista_equipos):
    clasificados = {"estandar" : [], "avanzado": []}
    for i in range (len(lista_equipos)):
        if lista_equipos[i] ["ram"] == 8:
            clasificados["estandar"].append(lista_equipos[i]["nombre"])
        else:
            clasificados["avanzado"].append(lista_equipos[i]["nombre"])

    return clasificados




def main():

    equipos = [
    {"nombre": "Dell XPS", "ram": 16},
    {"nombre": "ThinkPad T480", "ram": 8},
    {"nombre": "MacBook Pro", "ram": 32},
    {"nombre": "HP ProBook", "ram": 8},
    {"nombre": "ASUS TUF", "ram": 16}
              ]

    resultado = clasificar_equipos(equipos)

    print(resultado)




if __name__ == "__main__":
    main()