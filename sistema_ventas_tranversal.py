def mostrar_menu():
    print("======MENU PRINCIPAL=====")
    print("1. Registrar venta")
    print("2. Buscar producto por codigo")
    print("3. rebasteser stock")
    print("4. Eliminar producto.")
    print("5. Salir.")

def opcion_menu():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion >= 1 and opcion <= 5:
                return opcion
            else:
                print("Opcion no valida")
        except ValueError:
            print("Valor debe ser un numero entre 1 y 5.")

def buscar_codigo(ventas, codigo_buscar):
    if codigo_buscar in ventas:
        return codigo_buscar
    return -1

def validar_codigo(codigo):
    return(len(codigo.strip()) > 0)

def validar_stock(stock):
    return (stock > 0)

def rebasteser_stock(ventas):
    codigo = input("Ingrese el codigo que busca: ").upper()
    posicion = buscar_codigo(ventas, codigo)
    if posicion != -1:
        while True:
            try:
                nuevo_stock = int(input("Ingrese la nueva cantidad: "))
                if validar_stock (nuevo_stock):
                    ventas[posicion]['stock'] += nuevo_stock
                    print("Stock nuevo registrado")
                    break
                else:
                    print("El nuevo stock no puede ser 0")
            except ValueError:
                print("Numero debe ser entero")
    else:
        print("Codigo no esta registrado")

def eliminar_producto(ventas):
    codigo = input("Ingrese el codigo a eliminar: ").upper()
    posicion = buscar_codigo(ventas, codigo)
    if posicion != -1:
        ventas.pop(posicion)
        print("Producto eliminado")
    else:
        print("Producto no encontrado")

def registrar_venta (productos, ventas):
    codigo = input("Ingrese el codigo del producto que vendera: ").upper()
    posicion = buscar_codigo(productos, codigo)
    if posicion != -1:
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad a vender: "))
                if validar_stock (cantidad) and  cantidad <= productos[posicion]['stock']:
                    break
                else:
                    print("la cantidad no puede ser 0 o menor tampoco puede superar el stock.")
                    print(f"EL stock actual es: {productos[posicion]['stock']}")
            except ValueError:
                print("Valor debe ser un numero")

        total_pagar = productos[posicion]['precio'] * cantidad
        productos[posicion]['stock'] -= cantidad
        print(f"Total a pagar: {total_pagar}")
        nueva_clave = len(ventas) + 1
        ventas[nueva_clave]={'codigo_prod': codigo,
                             'cantidad': cantidad,
                             'total': total_pagar}

    
        print("Venta registrada")


def principal ():


    productos = {
    "PROD01": {"nombre": "Mouse Gamer", "precio": 15000, "stock": 10},
    "PROD02": {"nombre": "Teclado Mecánico", "precio": 45000, "stock": 5}
    }

    ventas = {
    1: {"codigo_prod": "PROD01", "cantidad": 2, "total": 30000}
    }

    while True:
        mostrar_menu()
        opcion = opcion_menu()

        if opcion == 1:
            registrar_venta(productos, ventas)
        elif opcion == 2:
            codigo = input("ingrese el codigo que busca: ").upper()
        
            posicion = buscar_codigo(productos,codigo)
            if posicion != -1:
                print("===== PRODUCTO ======")
                print(f"Nombre: {productos[codigo]['nombre']}")
                print(f"Precio: {productos[codigo]['precio']}")
                print(f"Stock: {productos[codigo]['stock']}")
            else:
                print("Codigo no encontrado")
            
        
        elif opcion == 3:
            rebasteser_stock(productos)

        elif opcion == 4:
            eliminar_producto(productos)

        elif opcion == 5:
            print("Gracias adios")
            break

        print(ventas)

if __name__ == "__main__":
    principal()