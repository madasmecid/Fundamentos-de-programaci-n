#=========================================================
#FUNCION QUE CUENTA CUANTO STOCK TIENE UNA MARCA INGRESADA
#=========================================================

def stock_marca(stock, productos, marca):
    stock_total = 0
    for modelo, detalle in productos.items():
        marca_detalle = detalle [0]
        if marca_detalle.lower()== marca.lower():
            stock_total += stock[modelo][1]

    return stock_total

#=========================================================
#FUNCIONES DE MENU Y SELECCION DE OPCION DE MENU
#=========================================================

def mostrar_menu():
    print ("*** MENU PRINCIPAL ***")
    print("1. Stock Marca.")
    print("2. Busqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

def opcion_menu():
    while True:
        opcion = input("Ingrese una opción: ")
        if opcion in ['1','2','3','4']:
            return int(opcion)
        print("Opción no valida. Intente nuevamente.")

#=========================================================
#FUNCION BUSQUEDA PRECIO EN RANGO
#=========================================================
def busqueda_precio(stock, productos, p_min, p_max):
    stock_bueno = []
    for modelo , detalle in stock.items():
        if modelo in productos:
            precio = detalle[0]
            stock_actual = detalle [1]
            if (precio >= p_min and precio <= p_max) and stock_actual > 0:
                stock_bueno.append(f"{productos [modelo][0]} -- {modelo}")

    return stock_bueno
#=========================================================
#FUNCION ACTUALIZAR PRECIO
#=========================================================

def actualizar_precio(stock, modelo, precio):
    if modelo in stock:
        stock[modelo][0] = precio
        return True

#=========================================================
#FUNCIÓN PRINCIPAL
#=========================================================

def sistema_central():
    

    productos = {
                '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
                'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
                }
    stock = {
        '8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
                }
    while True:
        mostrar_menu()
        opcion = opcion_menu()

        if opcion == 1:

            marca = input("Ingrese marca: ")
            total = stock_marca(stock, productos, marca)

            if total > 0:
                print(f"EL stock total es: {total}")
            else:
                print("No existe stock de esa marca.")

        elif opcion == 2:
            p_min = int(input("Ingrese el precio minimo: "))
            p_max = int(input("ingrese el precio maximo: "))
            disponibles = busqueda_precio(stock, productos, p_min, p_max)

            if disponibles:
                print(disponibles)
            else:
                print("No hay productos en este rango.")

        elif opcion == 3:
            while True:
                modelo = input("ingrese el modelo que quiere actualizar precio: ")
                try:
                    precio = int(input("Ingrese el precio nuevo: "))
                except ValueError:
                    print("Debe ser un valor numerico entero.")
                    continue
                    

                actualizado = actualizar_precio(stock, modelo, precio)

                if actualizado:
                    print("Precio actualizado.")
                else:
                    print("Precio no se actualizo.")

                seguir = input("Quiere seguir actualizando? (s/n): ")
                if seguir == "n":
                    break
                else:
                    continue

        elif opcion == 4:
            print("Hasta prontro gracias por usar nuestro programa.")
            break
            
        
        

        





if __name__ == "__main__":
    sistema_central()