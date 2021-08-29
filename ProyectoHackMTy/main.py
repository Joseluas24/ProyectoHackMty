import tkinter as tk
from tkinter import *
from tkinter import Button
from PIL import ImageTk, Image
import webbrowser
import sys
import urllib.request
import urllib.request as rq
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import *
import time

# OutPut es dN...
# Valor Personas
g1 = 9
g2 = 9
g3 = 9
g4 = 9
g5 = 9
g6 = 9
g7 = 9

# Time
now = datetime.now().time()
hora = (now.hour)
print("Hora Buscada", hora)
hora = str(hora) + ":00"
if len(hora) < 5:
    hora = "0" + hora

class Mall:
    def __init__(self, url):
        self.url = url
        self.danger = 0

fashion_d = Mall("https://www.google.com.mx/maps/place/Fashion+Drive/@25.6512551,-100.3371793,17z/data=!3m2!4b1!5s0x8662be13259e16db:0xf0f00bfe304cc159!4m5!3m4!1s0x8662be133c7c1df7:0xab85d8fcb4d1f64a!8m2!3d25.6512503!4d-100.3349906")
paseo_s_p = Mall("https://www.google.com/maps/place/Paseo+San+Pedro/@25.6516322,-100.3615572,17z/data=!3m1!4b1!4m5!3m4!1s0x8662bde6495aeda3:0x68aa193dc0e5b8b7!8m2!3d25.6516274!4d-100.3593685")
avanta_g = Mall("https://www.google.com/maps/place/Avanta+Gardens+San+Pedro/@25.6573074,-100.3916582,17z/data=!3m1!4b1!4m5!3m4!1s0x8662bd9ca9c1a8db:0x63a6660a3e91907!8m2!3d25.6573026!4d-100.3894695")
punto_v = Mall("https://www.google.com/maps/place/Punto+Valle+(The+Town+Center)/@25.6588985,-100.3569652,17z/data=!3m2!4b1!5s0x8662bde35e15fc3d:0x53ab072b8933e106!4m5!3m4!1s0x8662bde4a2974b07:0xaa5d5ac3f0904ee6!8m2!3d25.6588937!4d-100.3547765")
plaza_n = Mall("https://www.google.com/maps/place/Plaza+Nativa/@25.6597624,-100.4176931,17z/data=!3m1!4b1!4m5!3m4!1s0x8662bd670ce02077:0xda5f9c435700b22a!8m2!3d25.6597576!4d-100.4155044")
plaza_xo = Mall("https://www.google.com.mx/maps/place/Plaza+XO/@25.6599745,-100.3721168,17z/data=!3m1!4b1!4m5!3m4!1s0x8662bdacd1695f95:0xbf3e6a5c4ab2c58d!8m2!3d25.6599769!4d-100.3699537")
plaza_lua = Mall("https://www.google.com.mx/maps/place/Plaza+L%C3%BAa/@25.6578389,-100.3555966,17z/data=!3m2!4b1!5s0x8662961587da46f3:0x558efe3406288a75!4m5!3m4!1s0x8662bde309df8415:0x137ec2b6cfc47622!8m2!3d25.6578292!4d-100.3534082")

plazas = [fashion_d, paseo_s_p, avanta_g, punto_v, plaza_n, plaza_xo, plaza_lua]

def info(datos, time):  # time is a nn:nn type string
    idx1 = datos.find(time)
    info = datos[(idx1 + 25):(idx1 + 70)]
    idx2 = info.find(',\\"Por lo general')
    info = info[0:idx2]

    return info

for plaza in plazas:
    time.sleep(2)
    datos = rq.urlopen(plaza.url).read().decode()
    info_string = info(datos, hora)

    try:
        plaza.danger = int(info_string)
        print(plaza.danger)
    except:
        plaza.danger = 0
        print("Sin datos")


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

# Cuadro Rojo
def lrojo(c_x, c_y):
    #photocuadrado_rojo = tk.PhotoImage(file="cuadrado_rojo.png")
    #photocuadrado_rojo = Image.open("cuadrado_rojo.png")
    #resized_rojo = photocuadrado_rojo.resize((10, 10), Image.ANTIALIAS)
    #photocuadrado_rojo = ImageTk.PhotoImage(resized_rojo)
    label_rojo = Label(root, image=photocuadrado_rojo)
    label_rojo.pack()
    label_rojo.place(relx=c_x, rely=c_y, anchor='center')

# Cuadro Naranja
def lnaranja(c_x, c_y):
    #photocuadrado_naranja = tk.PhotoImage(file="cuadrado_naranja.png")
    #photocuadrado_naranja = Image.open("cuadrado_naranja.png")
    #resized_naranja = photocuadrado_naranja.resize((10, 10), Image.ANTIALIAS)
    #photocuadrado_naranja = ImageTk.PhotoImage(resized_naranja)
    label_naranja = Label(root, image=photocuadrado_naranja)
    label_naranja.pack()
    label_naranja.place(relx=c_x, rely=c_y, anchor='center')

# Cuadro verde
def lverde(c_x, c_y):
    #photocuadrado_verde = tk.PhotoImage(file="cuadrado_verde.png")
    #photocuadrado_verde = Image.open("cuadrado_verde.png")
    #resized_verde = photocuadrado_verde.resize((10, 10), Image.ANTIALIAS)
    #photocuadrado_verde = ImageTk.PhotoImage(resized_verde)
    label_verde = Label(root, image=photocuadrado_verde)
    label_verde.pack()
    label_verde.place(relx=c_x, rely=c_y, anchor='center')

# Label Nombre Fashion Drive
label_fashion_drive = Label(root, text="Fashion Drive")
label_fashion_drive.pack(anchor=CENTER)
label_fashion_drive.config(fg="Black",  # Foreground
                           font=("Verdana", 6, 'bold'))
label_fashion_drive.place(relx=.835, rely=.53, anchor='center')

# Label Nombre Paseo San Pedro
label_paseo_san_pedro = Label(root, text="Paseo San Pedro")
label_paseo_san_pedro.pack(anchor=CENTER)
label_paseo_san_pedro.config(fg="Black",  # Foreground
                             font=("Verdana", 6, 'bold'))
label_paseo_san_pedro.place(relx=.685, rely=.54, anchor='center')

# Label Nombre Avanta Garden
label_avanta_garden = Label(root, text="Avanta Garden")
label_avanta_garden.pack(anchor=CENTER)
label_avanta_garden.config(fg="Black",  # Foreground
                          font=("Verdana", 6, 'bold'))
label_avanta_garden.place(relx=.5, rely=.46, anchor='center')

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

# Label Nombre Centro Lua
label_centro_lua = Label(root, text="Centro Lua")
label_centro_lua.pack(anchor=CENTER)
label_centro_lua.config(fg="Black",  # Foreground
                           font=("Verdana", 6, 'bold'))
label_centro_lua.place(relx=.66, rely=.62, anchor='center')


# Fashion Drive
if fashion_d.danger < 35:
    # label_verde
    lverde(.835, .56)

elif fashion_d.danger < 70:
    # label_naranja
    lnaranja(.835, .56)

else:
    # label_rojo
    lrojo(.835, .56)

# paseo_san_pedro
if paseo_s_p.danger < 35:
    # label_verde
    lverde(.685,.57)

elif paseo_s_p.danger < 70:
    # label_naranja
    lnaranja(.685,.57)

else:
    # label_rojo
    lrojo(.685,.57)

# plaza_Avanta Garden
if avanta_g.danger < 35:
    # label_verde
    lverde(.5, .48)

elif avanta_g.danger < 70:
    # label_naranja
    lnaranja(.5, .48)

else:
    # label_rojo
    lrojo(.5, .48)

# punto_valle
if punto_v.danger < 35:
    # label_verde
    lverde(.712, .45)

elif punto_v.danger < 70:
    # label_naranja
    lnaranja(.712,.45)

else:
    # label_rojo
    lrojo(.712,.45)

# plaza_nativa
if plaza_n.danger < 35:
    # label_verde
    lverde(.312,.45)

elif plaza_n.danger < 70:
    # label_naranja
    lnaranja(.312,.45)

else:
    # label_rojo
    lrojo(.312,.45)

# plaza_xo
if plaza_xo.danger < 35:
    # label_verde
    lverde(.612,.45)

elif plaza_xo.danger < 70:
    # label_naranja
    lnaranja(.612,.45)

else:
    # label_rojo
    lrojo(.612,.45)

# Centro Lua
if plaza_lua.danger < 35:
    # label_verde
    lverde(.66, .64)

elif plaza_lua.danger < 70:
    # label_naranja
    lnaranja(.66, .64)

else:
    # label_rojo
    lrojo(.66, .64)

root.mainloop()
