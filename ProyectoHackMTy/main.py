import tkinter as tk
from tkinter import *
from tkinter import Button
from PIL import ImageTk, Image
import webbrowser
import sys
import urllib.request
import urllib.request as rq
from bs4 import BeautifulSoup

g1 = 9
g2 = 5
g3 = 2
g4 = 9
g5 = 6
g6 = 0


datos = rq.urlopen("https://www.google.com.mx/maps/place/Fashion+Drive/@25.6512551,-100.3371793,17z/data=!3m2!4b1!5s0x8662be13259e16db:0xf0f00bfe304cc159!4m5!3m4!1s0x8662be133c7c1df7:0xab85d8fcb4d1f64a!8m2!3d25.6512503!4d-100.3349906").read().decode()
idx1 = datos.find('12:00')
print(idx1)
info = datos[(idx1):(idx1+78)]
idx2 = info.find("Por lo general")
idx3 = info.find("concurrido")
info = info[idx2:(idx3 + 10)]
print(info)

# Canvas
root = tk.Tk()
root.config(bg="White smoke")
root.title("Inerfaz 1.0")
root.minsize(width=1025, height=545)
root.maxsize(width=1025, height=545)

# Imagen del mapa
photo = tk.PhotoImage(file="funciona.png")
photo = Image.open("map.png")
resized_map = photo.resize((1025, 545), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_map)

# Label fondo
label = Label(root, image=photo)
label.pack()
label.place(relx=.5, rely=.5, anchor='center')

# Centros comerciales
fashion_drive = g1
paseo_san_pedro = g2
plaza_saaghi = g3
punto_valle = g4
plaza_nativa = g5
plaza_xo = g6

# Cuadro Rojo
photocuadrado_rojo = tk.PhotoImage(file="cuadrado_rojo.png")
photocuadrado_rojo = Image.open("cuadrado_rojo.png")
resized_rojo = photocuadrado_rojo.resize((10, 10), Image.ANTIALIAS)
photocuadrado_rojo = ImageTk.PhotoImage(resized_rojo)

# Cuadro Naranja
photocuadrado_naranja = tk.PhotoImage(file="cuadrado_naranja.png")
photocuadrado_naranja = Image.open("cuadrado_naranja.png")
resized_naranja = photocuadrado_naranja.resize((10, 10), Image.ANTIALIAS)
photocuadrado_naranja = ImageTk.PhotoImage(resized_naranja)

# Cuadro verde
photocuadrado_verde = tk.PhotoImage(file="cuadrado_verde.png")
photocuadrado_verde = Image.open("cuadrado_verde.png")
resized_verde = photocuadrado_verde.resize((10, 10), Image.ANTIALIAS)
photocuadrado_verde = ImageTk.PhotoImage(resized_verde)

# Label Nombre Fashion Drive
label_fashion_drive = Label(root, text="Fashion Drive")
label_fashion_drive.pack(anchor=CENTER)
label_fashion_drive.config(fg="Black",  # Foreground
                           font=("Verdana", 6, 'bold'))
label_fashion_drive.place(relx=.835, rely=.53, anchor='center')

# Label Nombre Paseo San Pedrp
label_paseo_san_pedro = Label(root, text="Paseo San Pedro")
label_paseo_san_pedro.pack(anchor=CENTER)
label_paseo_san_pedro.config(fg="Black",  # Foreground
                             font=("Verdana", 6, 'bold'))
label_paseo_san_pedro.place(relx=.685, rely=.54, anchor='center')

# Label Nombre Plaza Saaghi
label_plaza_saaghi = Label(root, text="Plaza Saaghi")
label_plaza_saaghi.pack(anchor=CENTER)
label_plaza_saaghi.config(fg="Black",  # Foreground
                          font=("Verdana", 6, 'bold'))
label_plaza_saaghi.place(relx=.80, rely=.57, anchor='center')

# Label Nombre Punto Valle
label_punto_valle = Label(root, text="Punto Valle")
label_punto_valle.pack(anchor=CENTER)
label_punto_valle.config(fg="Black",  # Foreground
                         font=("Verdana", 6, 'bold'))
label_punto_valle.place(relx=.712, rely=.42, anchor='center')

# Label Nombre Plaza Nativa
label_plaza_nativa = Label(root, text="Plaza Nativa")
label_plaza_nativa.pack(anchor=CENTER)
label_plaza_nativa.config(fg="Black",  # Foreground
                          font=("Verdana", 6, 'bold'))
label_plaza_nativa.place(relx=.312, rely=.43, anchor='center')

# Label Nombre Plaza XO
label_plaza_xo = Label(root, text="Plaza XO")
label_plaza_xo.pack(anchor=CENTER)
label_plaza_xo.config(fg="Black",  # Foreground
                      font=("Verdana", 6, 'bold'))
label_plaza_xo.place(relx=.612, rely=.43, anchor='center')

# Fashion Drive
if fashion_drive < 5:
    # label_verde
    label_verde = Label(root, image=photocuadrado_verde)
    label_verde.pack()
    label_verde.place(relx=.835, rely=.56, anchor='center')

elif fashion_drive >= 5 and fashion_drive < 8:
    # label_naranja
    label_naranja = Label(root, image=photocuadrado_naranja)
    label_naranja.pack()
    label_naranja.place(relx=.835, rely=.56, anchor='center')

else:
    # label_rojo
    label_rojo = Label(root, image=photocuadrado_rojo)
    label_rojo.pack()
    label_rojo.place(relx=.835, rely=.56, anchor='center')

# paseo_san_pedro
if paseo_san_pedro < 5:
    # label_verde
    label_verde = Label(root, image=photocuadrado_verde)
    label_verde.pack()
    label_verde.place(relx=.685, rely=.57, anchor='center')

elif paseo_san_pedro >= 5 and paseo_san_pedro < 8:
    # label_naranja
    label_naranja = Label(root, image=photocuadrado_naranja)
    label_naranja.pack()
    label_naranja.place(relx=.685, rely=.57, anchor='center')

else:
    # label_rojo
    label_rojo = Label(root, image=photocuadrado_rojo)
    label_rojo.pack()
    label_rojo.place(relx=.685, rely=.57, anchor='center')

# plaza_saaghi
if plaza_saaghi < 5:
    # label_verde
    label_verde = Label(root, image=photocuadrado_verde)
    label_verde.pack()
    label_verde.place(relx=.80, rely=.6, anchor='center')

elif plaza_saaghi >= 5 and plaza_saaghi < 8:
    # label_naranja
    label_naranja = Label(root, image=photocuadrado_naranja)
    label_naranja.pack()
    label_naranja.place(relx=.80, rely=.6, anchor='center')

else:
    # label_rojo
    label_rojo = Label(root, image=photocuadrado_rojo)
    label_rojo.pack()
    label_rojo.place(relx=.80, rely=.6, anchor='center')

# punto_valle
if punto_valle < 5:
    # label_verde
    label_verde = Label(root, image=photocuadrado_verde)
    label_verde.pack()
    label_verde.place(relx=.712, rely=.45, anchor='center')

elif punto_valle >= 5 and punto_valle < 8:
    # label_naranja
    label_naranja = Label(root, image=photocuadrado_naranja)
    label_naranja.pack()
    label_naranja.place(relx=.712, rely=.45, anchor='center')

else:
    # label_rojo
    label_rojo = Label(root, image=photocuadrado_rojo)
    label_rojo.pack()
    label_rojo.place(relx=.712, rely=.45, anchor='center')

# plaza_nativa
if plaza_nativa < 5:
    # label_verde
    label_verde = Label(root, image=photocuadrado_verde)
    label_verde.pack()
    label_verde.place(relx=.312, rely=.45, anchor='center')

elif plaza_nativa >= 5 and plaza_nativa < 8:
    # label_naranja
    label_naranja = Label(root, image=photocuadrado_naranja)
    label_naranja.pack()
    label_naranja.place(relx=.312, rely=.45, anchor='center')

else:
    # label_rojo
    label_rojo = Label(root, image=photocuadrado_rojo)
    label_rojo.pack()
    label_rojo.place(relx=.312, rely=.45, anchor='center')

# plaza_xo
if plaza_xo < 5:
    # label_verde
    label_verde = Label(root, image=photocuadrado_verde)
    label_verde.pack()
    label_verde.place(relx=.612, rely=.45, anchor='center')

elif plaza_xo >= 5 and plaza_xo < 8:
    # label_naranja
    label_naranja = Label(root, image=photocuadrado_naranja)
    label_naranja.pack()
    label_naranja.place(relx=.612, rely=.45, anchor='center')

else:
    # label_rojo
    label_rojo = Label(root, image=photocuadrado_rojo)
    label_rojo.pack()
    label_rojo.place(relx=.612, rely=.45, anchor='center')

root.mainloop()
