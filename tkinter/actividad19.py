import tkinter as tk
from tkinter import messagebox

def mostrar_resultado(tipo_caixa, resultado):
    if resultado:
        etiqueta.config(text=f'Has clicat si ({tipo_caixa})', fg="green")  # Cambio el color del texto a verde si es "si"
    else:
        etiqueta.config(text=f'Has clicat no ({tipo_caixa})', fg="red")  # Cambio el color del texto a rojo si es "no"

def abrir_caixa_askyesno():
    var_resultado = messagebox.askyesno('Titol finestra', 'Missatge')
    mostrar_resultado("askyesno", var_resultado)

def abrir_caixa_askquestion():
    var_resultado = messagebox.askquestion('Titol finestra', 'Missatge')
    mostrar_resultado("askquestion", var_resultado)

def abrir_caixa_askokcancel():
    var_resultado = messagebox.askokcancel('Titol finestra', 'Missatge')
    mostrar_resultado("askokcancel", var_resultado)

def abrir_caixa_showinfo():
    messagebox.showinfo('Titol finestra', 'Missatge')
    etiqueta.config(text='Has clicat si (showinfo)', fg="blue")  # Cambio el color del texto a azul para showinfo

def abrir_caixa_showwarning():
    messagebox.showwarning('Titol finestra', 'Missatge')
    etiqueta.config(text='Has clicat si (showwarning)', fg="orange")  # Cambio el color del texto a naranja para showwarning

def abrir_caixa_showerror():
    messagebox.showerror('Titol finestra', 'Missatge')
    etiqueta.config(text='Has clicat si (showerror)', fg="purple")  # Cambio el color del texto a morado para showerror

# Crear la ventana principal
root = tk.Tk()
root.title('Ejercicio 3')
root.configure(bg="lightblue")  # Establezco un fondo de color azul claro

# Crear una etiqueta para mostrar los resultados
etiqueta = tk.Label(root, text='', fg="black")  # Texto negro por defecto
etiqueta.pack()

# Botones para abrir los diferentes cuadros de diálogo con colores modificados
btn_askyesno = tk.Button(root, text='AskYesNo', command=abrir_caixa_askyesno, bg="lightblue", fg="black")  # Fondo azul claro
btn_askquestion = tk.Button(root, text='AskQuestion', command=abrir_caixa_askquestion, bg="lightgreen", fg="black")  # Fondo verde claro
btn_askokcancel = tk.Button(root, text='AskOkCancel', command=abrir_caixa_askokcancel, bg="lightyellow", fg="black")  # Fondo amarillo claro
btn_showinfo = tk.Button(root, text='ShowInfo', command=abrir_caixa_showinfo, bg="lightcyan", fg="black")  # Fondo cian claro
btn_showwarning = tk.Button(root, text='ShowWarning', command=abrir_caixa_showwarning, bg="lightpink", fg="black")  # Fondo rosa claro
btn_showerror = tk.Button(root, text='ShowError', command=abrir_caixa_showerror, bg="lightcoral", fg="black")  # Fondo coral claro

btn_askyesno.pack()
btn_askquestion.pack()
btn_askokcancel.pack()
btn_showinfo.pack()
btn_showwarning.pack()
btn_showerror.pack()

root.mainloop()
