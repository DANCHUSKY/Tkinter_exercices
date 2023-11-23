from tkinter import ttk
import tkinter as tk
import os
from tkinter import filedialog as file_dialog
from tkinter import messagebox
from PIL import Image, ImageTk

# Función para guardar una imagen en un formato diferente
def guardar_imagen(imagen_origen):
    try:
        # Pedir al usuario una ubicación de archivo para guardar la imagen en formato PNG
        ruta_guardado = file_dialog.asksaveasfile(defaultextension=".png", filetypes=[("Archivos PNG", "*.png")])
        if ruta_guardado:
            # Convertir la imagen al modo RGB para eliminar la transparencia y luego guardarla como PNG
            imagen_origen = imagen_origen.convert('RGB')
            imagen_origen.save(ruta_guardado.name)
            messagebox.showinfo("¡Guardado!", "El archivo se ha guardado correctamente")
    except OSError as error:
        messagebox.showerror("Error", str(error))

# Función para gestionar la apertura de archivos
def gestionar_archivo():
    carpeta_fotos = "./fotos/"  # Ruta a la carpeta de fotos
    archivo = file_dialog.askopenfilename(initialdir=carpeta_fotos, filetypes=[("Imágenes", "*.jpg *.png")])

    if archivo:
        ventana_superior = tk.Toplevel()
        imagen_origen = Image.open(archivo)
        imagen_tk = ImageTk.PhotoImage(imagen_origen)

        etiqueta_imagen = tk.Label(ventana_superior, image=imagen_tk)
        etiqueta_imagen.image = imagen_tk
        etiqueta_imagen.pack()

        boton_guardar = ttk.Button(ventana_superior, text="Guardar imagen", command=lambda: guardar_imagen(imagen_origen))
        boton_guardar.pack()

app = tk.Tk()
app.title("Ejercicio 4")

# Configuración del estilo de los botones (fondo rosa claro)
estilo = ttk.Style()
estilo.configure('TButton', background='lightpink')

# Crear una etiqueta de texto y un botón en la ventana principal
tk.Label(text="Haz clic en el siguiente botón para seleccionar una imagen:", font=("Arial", 18)).grid(padx=15, pady=15)
ttk.Button(text="Abrir archivo", command=gestionar_archivo).grid(padx=15, pady=15)

app.mainloop()
