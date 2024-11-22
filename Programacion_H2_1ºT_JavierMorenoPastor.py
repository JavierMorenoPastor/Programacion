import Programacion_H2_1T_JavierMorenoPastor_Funciones as fh
fh.registro()
print("------------------------")
print("\n1.Ver usuarios registrados.")
print("\n2.Comprar. ")
print("\n3.Ver compra. ")
opcion = input("\n¿Que opción deseas realizar? ")

if opcion == '1':
    fh.ver_registrados()

if opcion == '2':
    fh.comprar()

if opcion == '3':
    fh.ver_compra()


