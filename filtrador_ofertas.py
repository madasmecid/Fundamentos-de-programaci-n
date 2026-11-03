def aplicar_descuento(lista_precios):
    lista_ofertas = []
    for precio in lista_precios:
        if precio < 50:
            nuevo_precio = precio *0.90
            lista_ofertas.append(nuevo_precio)
    return lista_ofertas


def main():

    precios_originales = [120, 45, 80, 15, 60, 30]

    resultado = aplicar_descuento(precios_originales)

    print (resultado)


if __name__ == "__main__":
    main()