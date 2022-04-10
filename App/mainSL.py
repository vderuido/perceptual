import streamlit as sl
import os
import random
import numpy as np
import pandas as pd

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
        sl.title("Perceptual APP")



        with sl.sidebar:
            opcion=sl.selectbox("Escoja un apartado",("Tutorial","Test"))


        if opcion=="Tutorial":

            sl.header("Tutorial")
            sl.write("Escucha las tres siguientes parejas de audio para entender las posibles situaciones que pueden darse en el experimento.")
            caso1,caso2,caso3=sl.columns(3)

            with caso1:
                sl.subheader("Caso 1")
                audio_file = open('/home/vic/Documents/universidad/PFM/Audios/tutorial/F1B2.wav', 'rb')
                audio_bytes = audio_file.read()

                sl.audio(audio_bytes, format='audio/wav')

                audio_file = open('/home/vic/Documents/universidad/PFM/Audios/tutorial/F1B2.wav', 'rb')
                audio_bytes = audio_file.read()

                sl.audio(audio_bytes, format='audio/wav')
            with caso2:
                sl.subheader("Caso 2")
                audio_file = open('/home/vic/Documents/universidad/PFM/Audios/tutorial/F1B2.wav', 'rb')
                audio_bytes = audio_file.read()

                sl.audio(audio_bytes, format='audio/wav')

                audio_file = open('/home/vic/Documents/universidad/PFM/Audios/tutorial/F1B2.wav', 'rb')
                audio_bytes = audio_file.read()

                sl.audio(audio_bytes, format='audio/wav')

            with caso3:
                sl.subheader("Caso 3")
                audio_file = open('/home/vic/Documents/universidad/PFM/Audios/tutorial/F1B2.wav', 'rb')
                audio_bytes = audio_file.read()

                sl.audio(audio_bytes, format='audio/wav')

                audio_file = open('/home/vic/Documents/universidad/PFM/Audios/tutorial/F1B2.wav', 'rb')
                audio_bytes = audio_file.read()

                sl.audio(audio_bytes, format='audio/wav')

        if opcion=="Test":

            numero=1
            sl.header("Test")
            sl.write("Audio ", numero, " de 5")
            caso1,caso2=sl.columns(2)

            with caso1:
                sl.subheader("Audio 1")
                audio_file = open('/home/vic/Documents/universidad/PFM/Audios/tutorial/F1B2.wav', 'rb')
                audio_bytes = audio_file.read()

                sl.audio(audio_bytes, format='audio/wav')

            with caso2:
                sl.subheader("Audio 2")
                audio_file = open('/home/vic/Documents/universidad/PFM/Audios/tutorial/F1B2.wav', 'rb')
                audio_bytes = audio_file.read()

                sl.audio(audio_bytes, format='audio/wav')

            sl.subheader("¿Lo tienes?, ¡genial! Ahora a responder.")
            respuesta = sl.radio(
                "Los audios son...",
                ('Iguales', 'Diferentes'))
            pulsado=False
            if sl.button("Enviar"):
                pulsado==True
            if pulsado==True:
                numero=numero+1
                pulsado=False

            sl.write(numero)

if __name__ =='__main__':
    main=Main()
