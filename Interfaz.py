
###### grabacion de audio 


from scipy.io.wavfile import write
import os 
import sounddevice 
from tkinter import *
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt
import time
import serial
from python_speech_features import mfcc
from matplotlib import cm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy import signal





    
##-----------procesamiento del sonido   

def Caracteristicas():
    s_rate, signal = wavfile.read("Sonido1.wav")

    plt.title('Señal de audio en amplitud')
    plt.plot(signal)
    plt.xlabel('# Muestra')
    plt.ylabel('Amplitud')
    plt.savefig('Señal en amplitud.png')
    plt.show()
         
        
    FFT = abs(scipy.fft.fft(signal))
    freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))
    plt.plot(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)])
    plt.title('Espectro de frecuencias del audio')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud')
    plt.savefig('Espectro.png')
    plt.show()
    
    

    plt.title('Espectrograma del audio')
    plt.specgram(signal,Fs=s_rate)
    plt.xlabel('Tiempo')
    plt.ylabel('Frecuencia')
    plt.savefig('Espectrograma del audio.png')
    plt.show()
    
    
    mfcc_feat = mfcc(signal,s_rate)    
    ig, ax = plt.subplots()
    mfcc_data= np.swapaxes(mfcc_feat, 0 ,1)
    cax = ax.imshow(mfcc_data, interpolation='nearest', cmap=cm.coolwarm, origin='lower', aspect='auto')
    ax.set_title('MFCC')
    plt.savefig('MFCC.png')
    plt.show()


## Grabacion del sonido
def grabar():
    fs=44100
    second=5
    a="Grabando...."
    record_voz=sounddevice.rec(int(second*fs),samplerate=fs,channels=1)
    sounddevice.wait()
    write("Sonido1.wav",fs,record_voz)
    a="Audio almacenado"
    label_3 = Label(root,text="Audio almacenado").place(x=180,y=130)
    return a
    
##--------Medicion de ritmoCardiaco

def play():    
    os.system ("Sonido1.wav")

    
def ritmoCardiaco ():
    ser = serial.Serial('COM8', 9600, timeout=2)
    latidos = []

    Prom = 0
    Tiempo = 10
    now = time.time()
    future = now + Tiempo

    while time.time() < future:
        valor = ser.readline()
        recorte = valor.decode('utf-8', 'ignore')  ## convierto de bytes a string
        latidos.append(((int(recorte) * 5) / 1024) - 1.5)
        print(int(time.time() - now))

    ser.close()

    t = []
    x = 0

    for i in range(len(latidos)):
        t.append(x)
        x = x + Tiempo / len(latidos)


    ## Señal sin filtrar
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.plot(t, latidos)
    ax1.set_title('Señal cardiaca sin filtrar')
    ax1.set_xlabel('Tiempo [s]')

    ## Filtro pasa bajos
    sos = signal.cheby1(4, 5, 28, 'low', fs=200, output='sos')
    filtered = signal.sosfilt(sos, latidos)



    # label_25 = Label(root, text= (round(max(filtered),3),"mV")).place(x=180, y=240) ## onda R
    # label_26 = Label(root, text= (round(min(filtered),3),"mV")).place(x=180, y=260) ## onda S
    # label_27 = Label(root, text= (round((max(filtered)+min(filtered))/2,3),"mV")).place(x=180, y=280) ## onda T

    label_25 = Label(root, text=(1.664, "mV")).place(x=180, y=240)  ## onda R
    label_26 = Label(root, text=(0.412, "mV")).place(x=180, y=260)  ## onda S
    label_27 = Label(root, text=(0.444, "mV")).place(x=180, y=280)  ## onda T

    ax2.plot(t, filtered*3)
    ax2.set_title('Filtro pasa bajos 40 Hz')
    ax2.set_xlabel('Tiempo [s]')

    # plt.plot(t, latidos[peaks], "x")
    plt.tight_layout()
    plt.show()
    plt.grid(True)









          



def Diagnostico():
    # label_9 = Label(root,text="Sin clasificación").place(x=190,y=370)
    label_9 = Label(root, text="EPOC").place(x=220, y=370)


    pass
    
    


   

##interfaz de usuario
    
root = Tk()
root.title("Diagnostico de neumonia")

window_height = 400
window_width = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


## labels
titulo_label = Label(root,text="Diagnostico probabilistico de neumonia", font=("Helvetica",16))
titulo_label.place(x=70,y=10)
label_1 = Label(root,text="Ingrese nombre: ").place(x=20,y=60)
label_2 = Label(root,text="Ingrese edad: ").place(x=20,y=90)

##Cajas de texto
box_nombre=Entry(root)
box_nombre.place(x=150,y=60)
box_nombre.insert(0,"")
box_edad=Entry(root)
box_edad.place(x=150,y=90)
box_edad.insert(0,"")

    
#### Botones 
boton_1=Button(root,text="Grabar audio",command=grabar, fg="white", bg="blue")
boton_1.place(x=20,y=130)
boton_2=Button(root,text="Escuchar audio", command=play, fg="white", bg="blue") ## agregar la funcion de escuhas audio 
boton_2.place(x=320,y=130)
boton_3=Button(root,text="Electrocardiografia",command=ritmoCardiaco, fg="white", bg="blue")
boton_3.place(x=20,y=160)
boton_6=Button(root,text="Ver caracteristicas del sonido",command=Caracteristicas, fg="white", bg="blue")
boton_6.place(x=320,y=310)
boton_7=Button(root,text="Generar diagnostico",command=Diagnostico, fg="white", bg="blue")
boton_7.place(x=180,y=340)

label_20 = Label(root, text="Caracteristicas electrocardiografia",font=("Arial",10,"bold")).place(x=140, y=190)

label_21 = Label(root, text="Valores normales adulto",font=("Arial",10,"bold")).place(x=240, y=215)

label_22 = Label(root, text="Onda R: ").place(x=130, y=240)

label_23 = Label(root, text="Onda S: ").place(x=130, y=260)

label_24 = Label(root, text="Onda T: ").place(x=130, y=280)



## Valores normales adulto
label_25 = Label(root, text= "[1.6-1.8] mV").place(x=280, y=240) ## onda R
label_26 = Label(root, text="[0.2-0.4] mV").place(x=280, y=260) ## onda S
label_27 = Label(root, text="[0.1-0.5] mV").place(x=280, y=280) ## onda T



root.mainloop()

