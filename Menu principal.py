# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 22:00:54 2023

@author: LoboM
"""

import tkinter as tk
import subprocess

# Función para iniciar el juego
def iniciar_juego():
    # Iniciar el programa que proporcionaste
    subprocess.Popen(["python", "there is a murder among us.py"])

# Crear una ventana tkinter
ventana = tk.Tk()
ventana.title("Juego Clue")

# Crear un botón para iniciar el juego
boton_inicio = tk.Button(ventana, text="Iniciar Juego", command=iniciar_juego)
boton_inicio.pack()

# Iniciar el bucle principal de tkinter
ventana.mainloop()