print("1-Categoría")
print("2-Productos")
print("3-Salir")
tabla = int(input("Selecciona sobre la tabla que quieras operar: "))

import FuncionesCRUD as fcrud
fcrud.conectar_basedatos()


if tabla == 1:
    print("===Gestión de Categorías===")
    print("1-Crear una nueva categoría")
    print("2-Leer categorías existentes")
    print("3-Actualizar una categoría")
    print("4-Eliminar una categoría")
    print("5-Salir")
    while True:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            print("Has seleccionado crear una nueva categoría")
            fcrud.crear()

        elif opcion == 2:
            print("Has seleccionado leer categorías existentes")
            fcrud.leer()

        elif opcion == 3:
            print("Has seleccionado actualizar una categoría")
            fcrud.actualizar()

        elif opcion == 4:
            print("Has seleccionado eliminar una categoría")
            fcrud.eliminar()

        elif opcion == 5:
            print("apagando...")
            break

        else:
            print("Introduce una opción válida")

elif tabla == 2:
    print("---Gestión de Productos---")
    print("1-Añadir un producto nuevo")
    print("2-Leer productos existentes")
    print("3-Actualizar productos")
    print("4-Eliminar productos")
    print("5-Salir")
    while True:
        opcion2 = int(input("Seleccione la opción que deseas realizar: "))
        if opcion2 == 1:
            print("Has seleccionado añadir un producto nuevo")
            fcrud.crear_productos()

        elif opcion2 == 2:
            print("Has seleccionado leer productos")
            fcrud.leer_productos()

        elif opcion2 == 3:
            print("Has seleccionado actualizar un producto")
            fcrud.actualizar_productos()

        elif opcion2 == 4:
            print("Has seleccionado eliminar un producto")
            fcrud.eliminar_productos()

        elif opcion2 == 5:
            print("Apagando...")
            break
        
        else:
            print("Introduce un número válido")

elif tabla == 3:
    print("Apagando...")

else:
    print("Introduzca un número válido")


