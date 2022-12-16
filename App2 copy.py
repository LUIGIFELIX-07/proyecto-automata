import os
import tkinter as tk
from PIL import ImageTk, Image


def sol():

    C = 1
    L = 1
    V = 1
    P = 1
    cont = 0
    estInicial = [C, L, V, P]
    print(estInicial)
    estAceptacion = [0, 0, 0, 0]
    while estInicial != estAceptacion:
        # devuelve al campesino
        if (C == 0 and L != V and V != P):
            C = 1
            estInicial = [C, L, V, P]
        # pasa campseino y lobo
        elif (C == 1) and (L == 1) and (V != P):
            C = 0
            L = 0
            estInicial = [C, L, V, P]
        # pasa campesino y pasto
        elif (C == 1) and (P == 1) and (V != L):
            C = 0
            P = 0
            estInicial = [C, L, V, P]
        # pasa campseino y oveja
        elif (C == 1) and (V == 1):
            C = 0
            V = 0
            estInicial = [C, L, V, P]
        # devuelve campesino y pasto
        elif (C == 0) and (P == 0) and (L != V):
            C = 1
            P = 1
            estInicial = [C, L, V, P]

        # devuelve campseino y oveja
        elif (C == 0) and (V == 0) and (P != L):
            C = 1
            V = 1
            estInicial = [C, L, V, P]
        print(estInicial)


root = tk.Tk()
## se cargan las imagenes desde la ruta a las variables
carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")
fondoRio = ImageTk.PhotoImage(Image.open(
    os.path.join(carpeta_imagenes, "ImagenRio.jpg")))
lobo = ImageTk.PhotoImage(Image.open(os.path.join(
    carpeta_imagenes, "Lobo.png")).resize((100, 100)))
pasto = ImageTk.PhotoImage(Image.open(os.path.join(
    carpeta_imagenes, "Heno.jpg")).resize((100, 100)))
campesino = ImageTk.PhotoImage(Image.open(os.path.join(
    carpeta_imagenes, "Campesino.jpg")).resize((100, 100)))
oveja = ImageTk.PhotoImage(Image.open(os.path.join(
    carpeta_imagenes, "Oveja.jpg")).resize((100, 100)))

# Interfaz
canvas1 = tk.Canvas(root, width=600, height=600)
canvas1.pack(fill="both", expand=False)
canvas1.create_image(0, 0, image=fondoRio, anchor="nw")
mostrarLobo = tk.Label(image=lobo)
mostrarOveja = tk.Label(image=oveja)
mostrarPasto = tk.Label(image=pasto)
mostrarCampesino = tk.Label(image=campesino)
canvas1.create_window(100, 75, window=mostrarLobo)
canvas1.create_window(100, 200, window=mostrarOveja)
canvas1.create_window(100, 325, window=mostrarCampesino)
canvas1.create_window(100, 450, window=mostrarPasto)
boton = tk.Button(text="Iniciar", bg="#88F242", command=sol)
boton.place(width=80, height=50,  x=100, y=525)


root.mainloop()
