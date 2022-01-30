#import pyaudio
#import wave
import numpy as np
import pandas as pd
#import matplotlib.pyplot
import os
import random
from playsound import playsound
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from gi.repository import Gdk

## DEFINICIÓN DE FUNCIONES

# Función que devuelve una lista con los archivos dentro de un directorio
def listaArchivos(ruta):
    archivos = os.listdir(ruta)
    return archivos

# Función que reproduce un archivo aleatorio dentro de los existentes dentro de un directorio que se le pasa como parámetro
def reproduceAudio(ruta, archivos, indice):
    print('Estamos reproduciendo: '+archivos[indice])
    #sonido=wave.open(ruta+'/'+archivos[indice])
    #reproducir(sonido)
    playsound(ruta+'/'+archivos[indice])


## Variables Globales
rutaTutorial='/home/vic/Documents/universidad/PFM/Audios/tutorial'
miruta='/home/vic/Documents/universidad/PFM/Audios/IRsTest'
misArchivosTutorial=listaArchivos(rutaTutorial)
misArchivos=listaArchivos(miruta)
respuestas=[None]
opcion=0
i=0
maximo=24
rutacsv='/home/vic/Documents/universidad/PFM/Resultados/test2.csv'
df=pd.DataFrame(
    {
        'archivo1': np.array(respuestas),
        'archivo2': np.array(respuestas),
        'respuesta': np.array(respuestas),
        'seguridad': np.array(respuestas),
    }
    )

miIndice1=random.randint(0,len(misArchivos)-1)
miIndice2=random.randint(0,len(misArchivos)-1)
df.iloc[0,0]=misArchivos[miIndice1]
df.iloc[0,1]=misArchivos[miIndice2]

iguales=False
seguridad=False

class Main:
    def __init__(self):
        gladeFile="appTFMGUITuto.glade"
        self.builder=gtk.Builder()
        self.builder.add_from_file(gladeFile)


        #Instanciar Ventana y botones tutorial
        wTutoWindow=self.builder.get_object("tutorialWindow")
        bSame1=self.builder.get_object("buttonSame1")
        bSame2=self.builder.get_object("buttonSame2")
        bDiferente1=self.builder.get_object("buttonDiferente1")
        bDiferente2=self.builder.get_object("buttonDiferente2")
        bFila1=self.builder.get_object("buttonFila1")
        bFila2=self.builder.get_object("buttonFila2")
        bStartTest=self.builder.get_object("buttonEmpezar")
        
        
        #Instancias Ventana y objetos ventana principal
        #wMainWindow=self.builder.get_object("mainWindow")
        bPlayAudio1=self.builder.get_object("PlayAudio1")
        bPlayAudio2=self.builder.get_object("PlayAudio2")
        sRespuesta=self.builder.get_object("SwitchRespuesta")
        sSeguridad=self.builder.get_object("SwitchSeguridad")
        bValidar=self.builder.get_object("ButtonValidar")


        #llamadas objetos
        
        ##Llamadas Ventana Tutorial
        wTutoWindow.connect("delete-event",gtk.main_quit)
        wTutoWindow.show()
        
        ##Llamadas botones tutorial
        bSame1.connect("clicked",self.botonSame1)
        bSame2.connect("clicked",self.botonSame1)
        bDiferente1.connect("clicked",self.botonSame1)
        bDiferente2.connect("clicked",self.botonDiferente2)
        bFila1.connect("clicked",self.botonSame1)
        bFila2.connect("clicked",self.botonFila2)
        bStartTest.connect("clicked",self.botonStartTest)
        
        #Llamadas Ventana Principal
        #wMainWindow.connect("delete-event",gtk.main_quit)
        #wMainWindow.show()

        #Llamadas Botones
        bPlayAudio1.connect("clicked", self.botonAudio1)
        bPlayAudio2.connect("clicked", self.botonAudio2)
        bValidar.connect("clicked",self.enviarRespuesta)

        #Llamadas Swithces
        sRespuesta.connect("notify::active", self.siPulsado)
        sSeguridad.connect("notify::active", self.siPulsadoSeguridad)
        
    # Funciones Interfaz Tutorial
    
    def botonSame1(self,widget):
        reproduceAudio(rutaTutorial, misArchivosTutorial, 1)
        
    def botonDiferente2(self,widget):
        reproduceAudio(rutaTutorial, misArchivosTutorial, 6)
        
    def botonFila2(self,widget):
        reproduceAudio(rutaTutorial, misArchivosTutorial, 5)
        
    def botonStartTest(self,widget):
        wMainWindow=self.builder.get_object("mainWindow")
        wMainWindow.connect("delete-event",gtk.main_quit)
        wMainWindow.connect("key-press-event", self.key_press)
        wMainWindow.show()
        
         
    # Funciones interfaz Test

    def key_press (self,window,event):
        keyname=Gdk.keyval_name(event.keyval)
        if keyname=="1":
            reproduceAudio(miruta, misArchivos, miIndice1)
            print("1 pulsado")
        if keyname=="2":
            reproduceAudio(miruta, misArchivos,miIndice2)
            print("2 pulsado")
            
    def botonAudio1(self, widget):
        print("Boton 1 pulsado")
        reproduceAudio(miruta, misArchivos, miIndice1)


    def botonAudio2(self,widget):
        print("Boton 2 pulsado")
        reproduceAudio(miruta, misArchivos,miIndice2)

    def siPulsado(self,widget,estado):
        global iguales
        if widget.get_active():
            iguales=True
        else:
            iguales=False
        print(iguales)

    def siPulsadoSeguridad(self,widget,estado):
        global seguridad
        if widget.get_active():
            seguridad=True
        else:
            seguridad=False
        print(seguridad)

    def enviarRespuesta(self,widget):
        global i
        global df
        global miIndice1
        global miIndice2

        txtTextPregunta=self.builder.get_object("TextPregunta")
        sRespuesta=self.builder.get_object("SwitchRespuesta")
        sSeguridad=self.builder.get_object("SwitchSeguridad")
        
        if iguales==False:
            df.iloc[0,2]=0
            print("Son diferentes")
        else:
            df.iloc[0,2]=1
            print("Son iguales")
        if seguridad==True:
            df.iloc[0,3]=1
            print("Respuesta segura")
        else:
            df.iloc[0,3]=0
            print("Respuesta insegura")
        if os.path.exists(rutacsv):
            print("El archivo ya existe, los resultados se añadirán al final del fichero.")
            df.to_csv(rutacsv, index=False, header=False, mode='a')
        else:
            print("El archivo no existe, se creará uno nuevo.")
            df.to_csv(rutacsv, index=False)
        if i<maximo:

            gtk.Label.set_text (txtTextPregunta, "Pregunta "+str(i+2)+" de 25: ¿Los audios son iguales?");
            i=i+1
            miIndice1=random.randint(0,len(misArchivos)-1)
            miIndice2=random.randint(0,len(misArchivos)-1)
            df.iloc[0,0]=misArchivos[miIndice1]
            df.iloc[0,1]=misArchivos[miIndice2]
            
            #Resetear switches
            sRespuesta.set_state(False)
            sSeguridad.set_state(False)
            
        else:
            gtk.Label.set_text (txtTextPregunta, "Test acabado. ¡Gracias!");

if __name__ =='__main__':
    main=Main()
    gtk.main()


