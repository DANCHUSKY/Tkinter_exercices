#Daniel Moreno Doncel

import tkinter as tk


num1 = None
operacion = None

# Esta función me permite borrar el cuadro de texto
def clear():
    entry.delete(0, tk.END)

# Al presionar un botón de operación, almaceno el número actual y la operación
def operar(tipo_operacion):
    global num1, operacion
    num1 = float(entry.get())  # Obtengo el primer número del cuadro de texto
    operacion = tipo_operacion  # Guardo la operación seleccionada
    clear()  # Borro el cuadro de texto para ingresar el segundo número

# Cuando presiono "=", realizo la operación y muestro el resultado
def igual():
    num2 = float(entry.get())  # Obtengo el segundo número del cuadro de texto
    resultado = None
    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error: División por cero"
    clear()  # Borro el cuadro de texto
    entry.insert(0, str(resultado))  # Muestro el resultado en el cuadro de texto

# Configuro la ventana
root = tk.Tk()  # Creo una ventana
root.title("Calculadora // Ejercicio 1")  # Establezco el título de la ventana
root.configure(bg="lightblue")  # Establezco un fondo de color azul claro

# Creo un cuadro de texto para mostrar los números y resultados
entry = tk.Entry(root, width=20)  # Creo un cuadro de texto
entry.grid(row=0, column=0, columnspan=4)  # Lo ubico en la ventana

# Creo botones para los números
for i in range(10):
    button = tk.Button(root, text=str(i), command=lambda i=i: entry.insert(tk.END, str(i))
                      , bg="lightgray")  # Botones con fondo gris claro
    button.grid(row=i // 3 + 2, column=i % 3)

# Creo botones para las operaciones (+, -, *, /)
operaciones = ["+", "-", "*", "/"]
for i, operacion in enumerate(operaciones):
    button = tk.Button(root, text=operacion, command=lambda operacion=operacion: operar(operacion)
                      , bg="lightgray")  # Botones con fondo gris claro
    button.grid(row=i + 2, column=3)

# Creo un botón igual (=) para calcular el resultado
button_igual = tk.Button(root, text="=", command=igual, bg="lightgreen")  # Botón con fondo verde claro
button_igual.grid(row=5, column=2)

# Creo un botón de borrar (C) para limpiar el cuadro de texto
button_clear = tk.Button(root, text="C", command=clear, bg="lightcoral")  # Botón con fondo coral claro
button_clear.grid(row=1, column=0)

root.mainloop()  
