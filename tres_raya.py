import tkinter as tk
from tkinter import messagebox

# Ventana principal
root = tk.Tk()
root.title("Tres en Raya - Lucrack Edition")

# Variables globales
turno = "X"
tablero = [""] * 9


# Función para manejar clics
def click(boton, i):
    global turno
    if tablero[i] == "":
        boton.config(text=turno, state="disabled")
        tablero[i] = turno
        if verificar_ganador(turno):
            messagebox.showinfo("Fin del juego", f"¡Ganó {turno}!")
            reiniciar()
        elif "" not in tablero:
            messagebox.showinfo("Fin del juego", "¡Empate!")
            reiniciar()
        else:
            turno = "O" if turno == "X" else "X"


# Verifica si alguien ganó
def verificar_ganador(jugador):
    combinaciones = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  # filas
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # columnas
        [0, 4, 8],
        [2, 4, 6],  # diagonales
    ]
    for combo in combinaciones:
        if all(tablero[i] == jugador for i in combo):
            return True
    return False


# Reiniciar juego
def reiniciar():
    global turno, tablero
    turno = "X"
    tablero = [""] * 9
    for i in range(9):
        botones[i].config(text="", state="normal")


# Crear botones del tablero
botones = []
for i in range(9):
    b = tk.Button(
        root,
        text="",
        width=10,
        height=4,
        font=("Arial", 20),
        command=lambda i=i: click(botones[i], i),
    )
    b.grid(row=i // 3, column=i % 3)
    botones.append(b)

root.mainloop()
