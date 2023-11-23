import sqlite3
import tkinter as tk

# Conecto a la base de datos SQLite y creo una tabla si no existe
var_BD = sqlite3.connect("base_de_datos/basquet.db")
cur_BD = var_BD.cursor()
cur_BD.execute("""
    CREATE TABLE jugado (
        nom TEXT,
        cognom TEXT,
        alçada REAL,
        edat INTEGER
    )
""")
var_BD.commit()
var_BD.close()

# Defino una función para insertar datos en la base de datos


def insertar_datos():
    # Conecto a la base de datos nuevamente
    var_BD = sqlite3.connect("base_de_datos/basquet.db")
    cur_BD = var_BD.cursor()
    # Obtengo los datos de los campos de entrada
    datos = {
        'z_nom': Entry_nom.get(),
        'z_cog': Entry_cognom.get(),
        'z_alçada': Entry_alçada.get(),
        'z_edat': Entry_edat.get()
    }
    # Ejecuto la inserción de datos en la tabla "jugadors"
    cur_BD.execute("""
        INSERT INTO jugadors (nom, cognom, alçada, edat)
        VALUES (:z_nom, :z_cog, :z_alçada, :z_edat)
    """, datos)
    var_BD.commit()
    var_BD.close()


# Creo una interfaz gráfica utilizando tkinter
root = tk.Tk()
root.title("Inserción de datos en la base de datos")

# Agrego etiquetas y campos de entrada
label_nom = tk.Label(root, text="Nombre:")
Entry_nom = tk.Entry(root)
label_cognom = tk.Label(root, text="Apellido:")
Entry_cognom = tk.Entry(root)
label_alçada = tk.Label(root, text="Altura:")
Entry_alçada = tk.Entry(root)
label_edat = tk.Label(root, text="Edad:")
Entry_edat = tk.Entry(root)

# Agrego un botón para insertar datos en la base de datos con color de fondo y texto personalizado
button_insertar = tk.Button(
    root, text="Insertar datos", command=insertar_datos, bg="green", fg="white")

# Organizo los elementos en la ventana
label_nom.grid(row=0, column=0)
Entry_nom.grid(row=0, column=1)
label_cognom.grid(row=1, column=0)
Entry_cognom.grid(row=1, column=1)
label_alçada.grid(row=2, column=0)
Entry_alçada.grid(row=2, column=1)
label_edat.grid(row=3, column=0)
Entry_edat.grid(row=3, column=1)
button_insertar.grid(row=4, columnspan=2)

# Establezco un color de fondo para la ventana principal
root.configure(bg="lightblue")

# Inicio la aplicación de la interfaz gráfica
root.mainloop()
