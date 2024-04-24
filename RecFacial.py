"""
Proyecto de reconocimiento facial
"""
#import time
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

"""
*******************************************
Invocacion para funciones
Invocar el abrir del reconocimiento facial
*******************************************
"""
def AbrirRecF():
    exec(open("prueba.py").read())
    print("Invocacion al rec")

"""
*******************************************
Configuracion de la pantalla
Color, imagen, tamaño, etc.
*******************************************
"""
interfaz = tk.Tk()
interfaz.title("Inicio de sesión")
interfaz.geometry("600x500")
interfaz.configure(bg= "#002C65") ##EF7F01 para el color naranja, #002C65 para el color azul
interfaz.resizable(False,False)

#Logo UPSLP
img = Image.open('imagenes/upslp.png')
img = img.resize((400,200))
render = ImageTk.PhotoImage(img)
img1 = Label(interfaz, image=render)
img1.image = render
img1.place(x=100, y=20)

#Logo Python
logo = Image.open('imagenes/python.png')
logo = logo.resize((40,40))
render = ImageTk.PhotoImage(logo)
img2 = Label(interfaz, image=render, bg="#002C65")
img2.image = render
img2.place(x=555, y=0)

"""
*******************************************
Implementacion de elementos
en la interfaz
Botones, Input, Labels, etc.
*******************************************
"""
Tx1 = Label(interfaz, text="Usuario", fg="White", font=("Arial", 20), bg="#002C65").place(x=100, y=270) #fg es para el color del texto

cTexto = tk.Entry(interfaz, font=("Arial",16))
cTexto.place(x=100, y=310)
b1 = tk.Button(interfaz, text="Iniciar\nReconocimiento", width=13, height=2, 
    bg="#EF7F01", font=("Arial Black",12), borderwidth=5, command=AbrirRecF) ##EF7F01 para el color naranja, #002C65 para el color azul
b1.place(x=200, y=400)

input()