#Daniel Moreno Doncel

import tkinter as tk
from PIL import Image, ImageTk
import os

# Obtengo la lista de imágenes en el directorio
directorio = "./fotos/"
imagenes = [archivo for archivo in os.listdir(directorio) if archivo.endswith(".png")]
imagen_actual = 0

# Función para mostrar la imagen actual
def mostrar_imagen():
    global imagen_actual
    imagen_path = os.path.join(directorio, imagenes[imagen_actual])
    img = Image.open(imagen_path)
    img = img.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    imagen_label.configure(image=img)
    imagen_label.image = img

    # Actualizo la etiqueta de la esquina inferior derecha
    etiqueta_info.config(text=f'Imatge {imagen_actual + 1} de {len(imagenes)}')

# Función para ir a la imagen anterior
def imagen_anterior():
    global imagen_actual
    if imagen_actual > 0:
        imagen_actual -= 1
        mostrar_imagen()

# Función para ir a la siguiente imagen
def imagen_siguiente():
    global imagen_actual
    if imagen_actual < len(imagenes) - 1:
        imagen_actual += 1
        mostrar_imagen()

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Ejercicio 2")

# Etiqueta para mostrar la imagen
imagen_label = tk.Label(ventana)
imagen_label.grid(row=0, column=0, columnspan=3)

# Botones con colores modificados
anterior_button = tk.Button(ventana, text="Imagen Anterior", command=imagen_anterior, bg="lightblue", fg="black")
siguiente_button = tk.Button(ventana, text="Siguiente Imagen", command=imagen_siguiente, bg="lightblue", fg="black")
salir_button = tk.Button(ventana, text="Salir", command=ventana.quit, bg="red", fg="white")

anterior_button.grid(row=1, column=0)
siguiente_button.grid(row=1, column=2)
salir_button.grid(row=1, column=1)

# Etiqueta para mostrar información de la imagen
etiqueta_info = tk.Label(ventana, bd=2, relief=tk.SUNKEN, anchor=tk.E)
etiqueta_info.grid(row=2, column=0, columnspan=3, sticky=tk.W + tk.E)

# Mostrar la primera imagen
mostrar_imagen()

ventana.mainloop()
