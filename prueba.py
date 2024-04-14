import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from prueba import * 

def AbrirRec():
    def cerrar():
        NuevaI.quit()
        NuevaI.destroy()
    NuevaI = tk.Tk()
    NuevaI.title("Reconocimiento facial")
    NuevaI.geometry("800x600")

    b1 = Button(NuevaI,text="Cerrar", command= cerrar).place(x=100, y=100)
