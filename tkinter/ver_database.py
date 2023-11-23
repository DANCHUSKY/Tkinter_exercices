import sqlite3

# Conecta a la base de datos
var_BD = sqlite3.connect("base_de_datos/basquet.db")
cur_BD = var_BD.cursor()

# Ejecuta una consulta SQL para seleccionar todos los datos de la tabla "jugadors"
cur_BD.execute("SELECT * FROM jugadors")

# Obtiene los resultados de la consulta
datos = cur_BD.fetchall()

# Cierra la conexión a la base de datos
var_BD.close()

# Imprime los datos en la consola
for dato in datos:
    print("Nombre:", dato[0])
    print("Apellido:", dato[1])
    print("Altura:", dato[2])
    print("Edad:", dato[3])
    print("\n")
