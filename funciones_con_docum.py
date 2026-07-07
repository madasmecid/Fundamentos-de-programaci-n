"""Funcion de validaciones, en estas funciones podemos validar distintas cosas como : el largo de una palabra, que un valor sea mayor o igual a 0, que un valor este
entre un rango, que una palabra contenga un caracter como por ejemplo el arroba, esta funcion retorna el valor que queremos validar y su argumento tambien es el valor ingresado"""
#=======================
#validaciones
#=======================
def validar_nombre(nombre):
    return(len(nombre.strip())> 0)
"""En esta función comprobamos que el largo sea mayor a 0 asi evitamos que no este vacio y si pone solo espacios los eliminamos con .strip()"""

def validar_paginas(paginas):
    return (paginas > 0)
"""En esta función validamos que la cantidad de algo no sea 0 o menor, en este caso es paginas de un libro ya que por logica no existen libros con 0 pagina"""

def validar_precio(precio):
    return(precio >= 0 )
""" Validamos el valor de algo con esta funcion, en este ejemplo es el precio del libro, este si puede ser 0 y ser regalado, pero no puedo ser -1"""

#=============================
#funciones principales
#=============================
"""En las funciones principales entra el menu y el seleccionador de opcion del menú,  el seleccionador de opcion trabaja dentro de un ciclo, 
ambas funciones no trabajan con argumento,
el menu solo es mostrar entonces trabaja solo con print y el seleccionador de menu trabaja con una entrada de datos (input)
esta recibe la opcion que quiere seleccionar el usuario, se crea una condicional, esta pregunta si el dato ingresado por el usuario esta dentro de una lista de opciones 
este retornara la opcion convertida en entero (int(opcion)) sino esta en la lista el dato ingresado por el usuario
se imprimira un mensaje de "opcion no valida, vuelva a intentar"""
def mostrar_menu():
    print("======================MENU PRINCIPAL=================")
    print("1- aagregar libro")
    print("2- Buscar libro")
    print("3- Eliminar libro")
    print("4- Actualizar libro")
    print("5- Mostrar libros")
    print("6- Salir")

def opcion_menu():
    while True:
        opcion = input("Ingrese una opcion: ")
        if opcion in ['1','2','3','4','5','6']:
            return int(opcion)
        print("Opcion no valida. Intente nuevamente")