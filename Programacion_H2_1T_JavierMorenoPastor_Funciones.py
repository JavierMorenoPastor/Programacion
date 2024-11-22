import random
import mysql.connector
def conectar_base_de_datos():
    conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="curso",
    database="hito2Python")
    if conexion.is_connected():
        print("---")
    return conexion
ids= set()

def registro():
    conexion = conectar_base_de_datos()
    cursor = conexion.cursor()
    print("--Registro--")
    nombre = str(input("\nIngresa tu nombre: "))
    telefono = int(input("\nIntroduce tu número de teléfono: "))
    correo = str(input("\nIngresa tu correo electrónico: "))
    id = random.randint(100,1000)
    print(f"Tu id es: {id}")
    consulta = "INSERT INTO registros(nombre, telefono, correo, id) VALUES (%s,%s,%s,%s)"
    cursor.execute(consulta, (nombre, telefono, correo, id))
    conexion.commit()
    print("registrado con éxito.")
    cursor.close()
    conexion.close


def ver_registrados():
    conexion = conectar_base_de_datos()
    cursor = conexion.cursor()
    consulta2 = "SELECT registros.nombre, registros.telefono, registros.correo, registros.id FROM registros"
    cursor.execute(consulta2)
    resultado = cursor.fetchall()
    print("Usuarios registrados: ")
    for usuarios in resultado:
        print(f"{usuarios}")
    cursor.close()
    conexion.close()

productos = {
    '1': "Leche",
    '2': "Zumo",
    '3': "Pan",
    '4': "Cereales",
    '5': "Sandía",
    '6': "Tortilla",
    '7': "Huevos",
    '8': "Agua",
    '9': "Sal",
    '10': "Azúcar",
}


def comprar():
    conexion = conectar_base_de_datos()
    cursor = conexion.cursor()
    print("\n--Productos--")
    print(productos)
    id_compra = random.randint(500,700)
    print(f"\nTu id de compra es: {id_compra}")
    comprar = (input("\nIntroduce Los códigos de los productos que deseas comprar: "))
    consulta = "INSERT INTO comprar(id_compra, id_producto) VALUES (%s,%s)"
    cursor.execute(consulta, (id_compra, comprar))
    conexion.commit()
    print("Productos añadidos al carrito correctamente.")
    cursor.close()
    conexion.close

def ver_compra():
    conexion = conectar_base_de_datos()
    cursor = conexion.cursor()
    print("\n--Seguimiento de pedido--")
    pedido = int(input("\nIngresa tu código de pedido: "))
    consulta3 = "SELECT compra.id_producto FROM compra"
    cursor.execute(consulta3, (pedido,))
    resultado = cursor.fetchall()
    if resultado:
        print("\nDatos del pedido: ")
        for id_compra, id_producto in resultado:
            print(f"Id del pedido: {id_compra}")
            print(f"Productos comprados: {id_producto}")
    else:
        print("\nNo se encontró un pedido con ese Id.")
    cursor.close()
    conexion.close()



    
    
    


