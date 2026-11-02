def analizar_precios(precios):
    precio_maximo = precios[0]
    precio_minimo = precios[0]
    for precio in precios:
        if precio > precio_maximo:
            precio_maximo = precio
   
        if precio <= precio_minimo:
            precio_minimo = precio

    return precio_maximo, precio_minimo


def main():

   precios = [12500, 3400, 45000, 890, 15000, 2300, 99900, 4500] 

   precio_max, precio_min = analizar_precios(precios)

   print(precio_max)
   print(precio_min)
if __name__ =="__main__":
    main()