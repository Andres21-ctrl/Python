from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog

Volumen = float(0.5)

#Functions
def Reproducir_cancion():
    archivo = filedialog.askopenfilename(initialdir="C:/", title="Por favor, seleccione un archivo")
    cancion_actual = archivo
    titulo_cancion = archivo.split("/")
    titulo_cancion = titulo_cancion[-1]

    try:
        mixer.init()
        mixer.music.load(cancion_actual)
        mixer.music.set_volume(Volumen)
        mixer.music.play()
        Ecancion_titulo.config(fg="green", text="Ahora sonando: " + str(titulo_cancion))
        E_volumen.config(fg="green", text="Volumen : " + str(Volumen))
    except Exception as e:
        print(e)
        Ecancion_titulo.config(fg="red", text="¡Error!, archivo incorrecto")

def reducir_volumen():
    try:
        global Volumen
        if Volumen <= 0:
            E_volumen.config(fg="red", text="Volumen : Muted")
            return
        Volumen = Volumen - float(0.1)
        Volumen = round(Volumen, 1)
        mixer.music.set_volume(Volumen)
        E_volumen.config(fg="green", text="Volumen : "+str(Volumen))
    except Exception as e:
        print(e)
        Ecancion_titulo.config(fg="red", text="La cancion no ha sido seleccionada aun")

def aumentar_volumen():
    try:
        global Volumen
        if Volumen >= 1:
            E_volumen.config(fg="green", text="Volumen : Max")
            return
        Volumen = Volumen + float(0.1)
        Volumen = round(Volumen, 1)
        mixer.music.set_volume(Volumen)
        E_volumen.config(fg="green", text="Volumen : "+str(Volumen))
    except Exception as e:
        print(e)
        Ecancion_titulo.config(fg="red", text="La cancion no ha sido seleccionada aun")

def Pausar():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        Ecancion_titulo.config(fg="red", text="La cancion no ha sido seleccionada aun")

def Reproducir():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        Ecancion_titulo.config(fg="red", text="La cancion no ha sido seleccionada aun")

#Main screen
ventana = Tk()
ventana.title("Reproductor de Musica")

#Labels
Label(ventana, text="Mi propio reproductor MP3", font=("Calibri", 15), fg="red").grid(sticky="N", row=0, padx=1)
Label(ventana, text="Por favor, seleccione una cancion que le gustaria escuchar", font=("Calibri", 12), fg="blue").grid(sticky="N", row=1)
Label(ventana, text="Volumen", font=("Calibri", 12), fg="red").grid(sticky="N", row=4)
Ecancion_titulo = Label(ventana, font=("Calibri", 12))
Ecancion_titulo.grid(sticky="N", row=3)
E_volumen = Label(ventana, font=("Calibri", 12))
E_volumen.grid(sticky="N", row=5)

#Buttons
Button(ventana, text="Escoja una cancion", font=("Calibri", 12), command=Reproducir_cancion).grid(row=2, sticky="N")
Button(ventana, text="Pausa", font=("Calibri", 12), command=Pausar).grid(row=3, sticky="E")
Button(ventana, text="Reanudar", font=("Calibri", 12), command=Reproducir).grid(row=3, sticky="W")
Button(ventana, text="+", font=("Calibri", 12), width=5, command=aumentar_volumen).grid(row=5, sticky="W")
Button(ventana, text="-", font=("Calibri", 12), width=5, command=reducir_volumen).grid(row=5, sticky="E")

ventana.mainloop()