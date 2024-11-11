import mysql.connector
def conectar_basedatos():
    conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="curso",
    database="SUPERMERCADO")
    if conexion.is_connected():
        print("---")
    return conexion

def crear():
    conexion = conectar_basedatos()
    cursor = conexion.cursor()
    nueva_categoriaID = input("\nEscribe el ID de la categoría: ")
    nueva_categoria = input("\nEscribe el nombre de la categoría:")
    consulta = "INSERT INTO CATEGORIA (idcategoria, categoria) VALUES(%s, %s)"
    cursor.execute(consulta, (nueva_categoriaID, nueva_categoria))
    conexion.commit()
    print("\nNueva categoría añadida")
    cursor.close()
    conexion.close()

def actualizar():
    conexion = conectar_basedatos()
    cursor = conexion.cursor()
    categoriaID = input("\nEscribe el ID de la categoría que quieras modificar: ")
    categoria = input("\nEscribe el nombre de la categoría que quieras modificar: ")
    consulta3 = "UPDATE categoria SET = %s WHERE idcategoria = %s"
    cursor.execute(consulta3, (categoriaID, categoria))
    conexion.commit()
    print("Cantidad actualizada correctamente")
    cursor.close()
    conexion.close()

def eliminar():
    conexion = conectar_basedatos()
    cursor = conexion.cursor()
    categoriaID = input("\nEscribe el nombre de la categoría que deseas eliminar: ")
    consulta4 = "DELETE FROM categoria where categoria = %s"
    cursor.execute(consulta4, (categoriaID,))
    conexion.commit()
    print("Categoría eliminada correctamente")
    cursor.close()
    conexion.close()

def leer():
    conexion = conectar_basedatos()
    cursor = conexion.cursor()
    consulta2 = """ SELECT categoria.categoria, categoria.idcategoria from categoria """
    cursor.execute(consulta2)
    resultados = cursor.fetchall()
    for categoria in resultados:
        print(f"categorias: {categoria}")
    cursor.close()
    conexion.close()

def crear_productos():
    conexion = conectar_basedatos()
    cursor = conexion.cursor()
    nuevo_productoID = input("\nEscribe el ID del producto: ")
    nuevo_producto = input("\nEscribe el nombre del nuevo producto:")
    nuevo_producto_precio = input("\nEscribe el precio del producto: ")
    nuevo_producto_stock = input("\nEscribe el stock del producto: ")
    consultap1 = "INSERT INTO PRODUCTO (idproducto, nombre, precio, stock) VALUES(%s, %s, %s, %s)"
    cursor.execute(consultap1, (nuevo_productoID, nuevo_producto, nuevo_producto_precio, nuevo_producto_stock))
    conexion.commit()
    print("\nNuevo producto añadido")
    cursor.close()
    conexion.close()

def leer_productos():
    conexion = conectar_basedatos()
    cursor = conexion.cursor()
    consultap2 = """ SELECT producto.nombre, producto.idproducto, producto.precio, producto.stock from producto """
    cursor.execute(consultap2)
    resultados = cursor.fetchall()
    for producto in resultados:
        print(f"Productos: {producto}")
    cursor.close()
    conexion.close()

def actualizar_productos():
    conexion = conectar_basedatos()
    cursor = conexion.cursor()
    productoID = input("\nEscribe el ID del producto que quieras modificar: ")
    producto = input("\nEscribe el nombre del producto que quieras modificar: ")
    consultap3 = "UPDATE producto SET nombre = %s WHERE idproducto = %s"
    cursor.execute(consultap3, (producto, productoID))
    conexion.commit()
    print("Cantidad actualizada correctamente")
    cursor.close()
    conexion.close()

def eliminar_productos():
    conexion = conectar_basedatos()
    cursor = conexion.cursor()
    productoID = input("\nEscribe el nombre del producto que deseas eliminar: ")
    consultap4 = "DELETE FROM producto where nombre = %s"
    cursor.execute(consultap4, (productoID,))
    conexion.commit()
    print("producto eliminado correctamente")
    cursor.close()
    conexion.close()








    






    
    
