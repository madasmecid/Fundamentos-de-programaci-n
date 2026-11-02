def analizar_precios(precios):
    precio_maximo = precios[0]
    precio_minimo = precios[0]
    for precio in precios:
        if precio > precio_maximo:
            precio_maximo = precio
        if precio <= precio_minimo:
            precio_minimo = precio
    return precio_maximo, precio_minimo

def precios_oferta(precios):
    lista_oferta = []
    promedio= 0
    cantidad_ofertas = 0
    precio_limite = 10000
    for precio in precios:
        if precio < precio_limite:
            lista_oferta.append(precio)
            cantidad_ofertas += 1
            promedio += precio

    if cantidad_ofertas > 0:
        resultado = promedio / cantidad_ofertas
    else:
        resultado = 0.0

    return lista_oferta, resultado


def main():

   precios = [12500, 3400, 45000, 890, 15000, 2300, 99900, 4500] 

   precio_max, precio_min = analizar_precios(precios)

   print(precio_max)
   print(precio_min)

   lista, resultado = precios_oferta(precios)

   print(f"La lista de ofertas es: {lista}")
   print(f"El promedio de precio de las ofertas es: {resultado}")


if __name__ =="__main__":
    main()