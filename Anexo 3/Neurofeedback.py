#se importa librerias
from math import pi
from tkinter import *
import tkinter as tk
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import brainflow
from brainflow.board_shim import BoardIds, BoardShim, BrainFlowInputParams
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk   
from matplotlib.figure import Figure
from scipy import signal
from numpy import arange
import scipy.signal
from spectrum import *
from scipy.signal import butter, lfilter


#definir algunas variavbles a utilizar
dcb="0"

#se poner paraametros y se obtiene señal eeg
def get_df(data):
    df = pd.DataFrame(data[:, [1,13]], columns=["ECG", "Time"])
    return df

def get_data(sfreq):
    try:
        while board.get_board_data_count() < sfreq:
            time.sleep(0.005)
    except Exception as e:
        raise(e)
    board_data = board.get_board_data()
    df = get_df(np.transpose(board_data))
    return df
#funcion de suma 
def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma

#funcion de filtro
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

 
#hace el cambio de marco destruye el anterior y crea el nuevo 
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------primera pantalla---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        bpriu=Button(self, text='Primera vez de usuario', height = 4, width = 20, command=lambda:master.switch_frame(PageOne))
        bpriu.grid(row=0, column=0, padx=100, pady=100, sticky="e")
        brsu=Button(self, text='Realizar sesión a usuario', height = 4, width = 20, command=lambda:master.switch_frame(PageTwo))
        brsu.grid(row=0, column=1, padx=100, pady=100, sticky="e")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
#--------------------------Obtencion de datos de usario----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        

        ##se obitenen datos de la personas y se guardan
        #agrega texto y cuadro para introducir informacion
        #Nombre
        nombrelabel= Label(self, text="Nombre:", fg="black", font=(10))
        nombrelabel.grid(row=0, column=0, padx=10, pady=10, sticky="e")


        nombrec= Entry(self, width=40)
        nombrec.grid(row=0, column=1, padx=10, pady=10)
        nombrec.config(justify="center")
        #Documento
        documentolabel= Label(self, text="Número de Documento:", fg="black", font=(10))
        documentolabel.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        documentoc= Entry(self, width=40)
        documentoc.grid(row=1, column=1, padx=10, pady=10)
        documentoc.config(justify="center")
        #Sexo
        sexolabel= Label(self, text="Sexo:", fg="black", font=(10))
        sexolabel.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        Sexoc= Entry(self, width=40)
        Sexoc.grid(row=2, column=1, padx=10, pady=10)
        Sexoc.config(justify="center")
        #Edad
        Edadlabel= Label(self, text="Edad:", fg="black", font=(10))
        Edadlabel.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        Edadc= Entry(self, width=40)
        Edadc.grid(row=3, column=1, padx=10, pady=10)
        Edadc.config(justify="center")
        #Nivel escolar
        nivelelabel= Label(self, text="Nivel escolar:", fg="black", font=(10))
        nivelelabel.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        nivelec= Entry(self, width=40)
        nivelec.grid(row=4, column=1, padx=10, pady=10)
        nivelec.config(justify="center")
        #Lateralidad
        Lateralidadlabel= Label(self, text="Lateralidad:", fg="black", font=(10))
        Lateralidadlabel.grid(row=5, column=0, padx=10, pady=10, sticky="e")

        Lateralidadc= Entry(self, width=40)
        Lateralidadc.grid(row=5, column=1, padx=10, pady=10)
        Lateralidadc.config(justify="center")
        #Diagnostico
        Diagnosticolabel= Label(self, text="Diagnóstico:", fg="black", font=(10))
        Diagnosticolabel.grid(row=6, column=0, padx=10, pady=10, sticky="e")

        Diagnosticoc= Entry(self, width=40)
        Diagnosticoc.grid(row=6, column=1, padx=10, pady=10)
        Diagnosticoc.config(justify="center")
        #Anotacion
        anotacionlabel= Label(self, text="Anotación:", fg="black", font=(10))
        anotacionlabel.grid(row=7, column=0, padx=10, pady=10, sticky="e")

        anotacion= Entry(self, width=40)
        anotacion.grid(row=7, column=1, padx=10, pady=10)
        anotacion.config(justify="center")


        def codigoboton():
            
            documentoo=documentoc.get()
            os.mkdir(documentoo) 
            d="\datos.txt"
            ubi=documentoo+d
            Datos=("Nombre:", "Documento:","Sexo:", "Edad:",nombrec.get(), documentoc.get(), Sexoc.get(),  Edadc.get(), 
                "Nivel Educativo:","Lateralidad:", "Diagnóstico:", "Anotación:",nivelec.get(), Lateralidadc.get() ,Diagnosticoc.get(), anotacion.get(),
                "#Sesión:", "Promedio:","Protocolo:", "Puntaje en juego:",)
            with open(ubi, 'w') as temp_file:
                for item in Datos:
                    temp_file.write("%s\n" % item)
            f = open ('sesion.txt','w')
            f.write(str(1))
            f.close()
            
            dcb=documentoc.get()
            f = open ('ud.txt','w')
            f.write(dcb)
            f.close()


        botondatos=Button(self, text="Guardar datos", command=lambda:[codigoboton(), master.switch_frame(Page4) ])
        botondatos.grid(row=8, column=1)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------Busqueda de usario--------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        

        buslabel= Label(self, text="Documento de Usuario:", fg="black", font=(10))
        buslabel.grid(row=0, column=0, padx=10, pady=10, sticky="e")


        documentob= Entry(self, width=40)
        documentob.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        
        def gdoc():

            dcb=documentob.get()
            f = open ('ud.txt','w')
            f.write(dcb)
            f.close()

        bbu=Button(self, text='Buscar', command=lambda:[gdoc(), master.switch_frame(PageT)])
        bbu.grid(row=1, column=1, padx=100, pady=100, sticky="e")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
#-------------------------------------muestra datos de usario buscado-------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class PageT(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        f = open ('ud.txt','r')
        dcb = str(f.read())
        f.close()
        d="\datos.txt"
        ubi=dcb+d
        #realiza tabla y lo muestra en gui
        i=0
        j=0
        archi1=open(ubi,"r")
        for linea in archi1:

            tabla= Label(self, text=linea, height=2, width=15, bg='white', fg="black", font=(10))
            tabla.grid(row=i, column=j, padx=10, pady=10, sticky="e")
            j+=1
            if j==4:
                i+=1
                j=0
        #guarda en que sesion va
        def numeros():
            archi1.close()
            rft=i-4
            rft=str(rft)
            f = open ('sesion.txt','w')
            f.write(rft)
            f.close()

        mdb=Button(self, text='Continuar', command=lambda:[numeros(), master.switch_frame(Page4)])
        mdb.grid(row=i, column=1, padx=10, pady=10, sticky="e", columnspan=2)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------Seleccion del nivel del juego-------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Page4(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        def escribir(nj):
            if nj==1:
                f = open ('nivel.txt','w')
                f.write(str(1))
                f.close()
            if nj==2:
                f = open ('nivel.txt','w')
                f.write(str(2))
                f.close()
            if nj==3:
                f = open ('nivel.txt','w')
                f.write(str(3))
                f.close()

        julabel= Label(self, text="Seleccione el nivel del Juego:", fg="black", font=(10))
        julabel.grid(row=0, column=1, padx=10, pady=10)    
        bscp=Button(self, text='Nivel 1 \n (Fácil)', height = 4, width = 20, command=lambda:[escribir(nj=1),master.switch_frame(Page5)])
        bscp.grid(row=1, column=0, padx=100, pady=100)
        btbr=Button(self, text='Nivel 2 \n (Medio)', height = 4, width = 20, command=lambda:[escribir(nj=2),master.switch_frame(Page5)])
        btbr.grid(row=1, column=1, padx=100, pady=100)
        bsmr=Button(self, text='Nivel 3 \n (Difícil)', height = 4, width = 20, command=lambda:[escribir(nj=3),master.switch_frame(Page5)])
        bsmr.grid(row=1, column=2, padx=100, pady=100)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------Seleccion del nivel del juego -------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Page5(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        julabel= Label(self, text="Seleccione el Protocolo a utilizar de acuerdo al tipo de TDAH", fg="black", font=(10))
        julabel.grid(row=0, column=1, padx=10, pady=10) 

        bscp=Button(self, text='SMR \n (Ritmo Sensoriomotor) \n Hiperactivo-Impulsivo', height = 4, width = 20, command=lambda:master.switch_frame(Pagesmr))
        bscp.grid(row=1, column=0, padx=100, pady=100)
        btbr=Button(self, text='TBR \n (Theta/Beta Ratio) \n Combinado', height = 4, width = 20, command=lambda:master.switch_frame(Pagetbr))
        btbr.grid(row=1, column=1, padx=100, pady=100)
        bsmr=Button(self, text='SCP \n (Slow Cortical Potentials) \n Inatento', height = 4, width = 20, command=lambda:master.switch_frame(Pagescp))
        bsmr.grid(row=1, column=2, padx=100, pady=100)

ecg = []
n = 250
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++-------------Protocolo smr----------------------------+++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Pagesmr(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        #VARIABLES Y DEFINICION DE PARAMETROS DE BRAINFLOW
        global board
        params = BrainFlowInputParams ()
        params.serial_port = ""
        board = BoardShim (BoardIds.SYNTHETIC_BOARD.value, params)
        board.prepare_session ()
        board.start_stream ()
        #variable para reiniciar
        self._job = None     
        ecg = []
        n = 200 #sfreq
        d=None
        f = open ('ud.txt','r')
        dcb = str(f.read())
        f.close()
        f = open ('sesion.txt','r')
        y=str(f.read())
        f.close()
#-----------------------------------SE PONEN GRAFICAS
        #---------SE OBTIENE SEÑAL EEG
        df = get_data(200)
        ecg.extend(df.iloc[:,0].values)


        #grafica EEG        
        f = plt.figure(figsize=(5,3), dpi=100)
        a = f.add_subplot(111)
        a.plot(ecg)
        dataPlot = FigureCanvasTkAgg(f, master=self)      
        dataPlot.get_tk_widget().grid(row=1, column=1,padx=15, pady=10, sticky="nsew")
        dataPlot.draw()
        
        #-------------transformacion de la señal EEG
        f, Pxx_den = signal.periodogram(ecg, 200)
        #grafica psd
        fr = plt.figure(figsize=(5,3), dpi=100)
        ar = fr.add_subplot(111)
        ar.plot(f, Pxx_den)
        dataPlot1 = FigureCanvasTkAgg(fr, master=self)      
        dataPlot1.get_tk_widget().grid(row=1, column=3, padx=15, pady=10, sticky="nsew")
        dataPlot1.draw()
        
        #-----------se obtiene las diferentes bandas
        deltap=sumalista(Pxx_den[1:4])
        thetap=sumalista(Pxx_den[5:7])
        alfap=sumalista(Pxx_den[8:12])
        betap=sumalista(Pxx_den[13:30])
        bandas=deltap, thetap, alfap, betap
        bandasname="Delta","Theta","Alfa","Beta"
        #grafica bandas
        fr1 = plt.figure(figsize=(5,3), dpi=100)
        ar1 = fr1.add_subplot(111)
        ar1.bar(bandasname, bandas)
        dataPlot2 = FigureCanvasTkAgg(fr1, master=self)      
        dataPlot2.get_tk_widget().grid(row=3, column=3, padx=15, pady=10, sticky="nsew")
        dataPlot2.draw()
        
        #---------------se obtiene scp
        SCPP=sumalista(Pxx_den[12:15])
        #grafica scp
        Pro="SMR"
        fr2 = plt.figure(figsize=(5,3), dpi=100)
        ar2 = fr2.add_subplot(111)
        ar2.bar(Pro, SCPP)
        dataPlot3 = FigureCanvasTkAgg(fr2, master=self)      
        dataPlot3.get_tk_widget().grid(row=3, column=1, padx=15, pady=10, sticky="nsew")
        dataPlot3.draw()

#---------------------------------------------------------------actualizar grafica
        def actuliazar():
            #eeg
            df = get_data(200)
            ecg.extend(df.iloc[:,0].values)

            #filtro notch de 60hz
            samp_freq = 200  
            notch_freq = 60.0  
            quality_factor = 60.0  
            b_notch, a_notch = signal.iirnotch(notch_freq, quality_factor, samp_freq)
            ecgt = signal.filtfilt(b_notch, a_notch, ecg)
            #filtro pasabanda
            bt, zt = butter_bandpass(0.5, 30, 200, order=6)
            ecgt = lfilter(bt, zt, ecgt) 

            ecgc=ecgt[len(ecg)-200:len(ecg)+200]      
            a.clear()
            a.plot(ecgc)
            dataPlot.draw()

            #PSD
            f, Pxx_den = signal.periodogram(ecgc, 200)
            ar.clear()
            ar.plot(f,Pxx_den)
            dataPlot1.draw()
            #Bandas
            deltap=sumalista(Pxx_den[1:4])
            thetap=sumalista(Pxx_den[5:7])
            alfap=sumalista(Pxx_den[8:12])
            betap=sumalista(Pxx_den[13:30])
            bandas=deltap, thetap, alfap, betap
            bandasname="Delta","Theta","Alfa","Beta"
            ar1.clear()
            ar1.bar(bandasname, bandas)
            
            dataPlot2.draw()
            #SCP
            SCPP=sumalista(Pxx_den[12:15])
            Pro="SMR" 
            ar2.clear()
            ar2.bar(Pro, SCPP)
            dataPlot3.draw()
            if SCPP>=4.9 and SCPP<=6.9:
                ttlabe22['text'] = "Concetrado"
                f = open ("estado.txt",'w')
                f.write("%s," % "Concentrado")
                f.write( str(SCPP))
                f.close()
            else:
                ttlabe22['text'] = "Desconcetrado"
                f = open ("estado.txt",'w')
                f.write("%s," % "Desconcentrado")
                f.write( str(SCPP))
                f.close()
            #guarda scp
            ddd="\sesion"+y+".txt"
            ubi=dcb+ddd
            f = open (ubi,'a')
            f.write("%s," % SCPP)
            f.close()

            #hace el bucle
            self._job = bscpp.after(1000, actuliazar)

        #-------funcion de parar el programa    
        def Parar():
            if self._job is not None:
                bscpp.after_cancel(self._job)
                self._job = None
        
        #------funcion de terminar
        def terminar():
            if self._job is not None:
                bscpp.after_cancel(self._job)
                self._job = None
            #guarda total de señal eeg
            d="\sesioneeg"+y+".txt"
            ubi=dcb+d
            with open(ubi, 'w') as temp_file:
                for item in ecg:
                    temp_file.write("%s\n" % item)
            #guarda promedio de protocolo en datos
            d=dcb+"\sesion"+y+".txt"
            f = open (d,'r')
            pp=f.read()
            f.close()            
            s=len(pp)
            prome=(sumalista(Pxx_den[13:30])/s)
            proto="SMR"
            f = open ("puntaje.txt",'r')
            pun=f.read()
            f.close() 
            f = open ("totalj.txt",'r')
            totalj=f.read()
            f.close() 
            punt=pun+"/"+totalj 
            ubi=dcb+"\datos.txt"
            f = open (ubi,'a')
            f.write("%s\n" % y)
            f.write("%s\n" % prome)
            f.write("%s\n" % proto)
            f.write("%s\n" % punt)
            f.close()
            
        #botones interfaz
        bscpi=Button(self, text='Inicio', height = 4, width = 20, command=lambda:actuliazar())
        bscpi.grid(row=5, column=0, padx=10, pady=10)
    
        bscpp=Button(self, text='Pausar', height = 4, width = 20, command=lambda:Parar() )
        bscpp.grid(row=5, column=1, padx=10, pady=10)

        bscpf=Button(self, text='Terminar', height = 4, width = 20, command=lambda:[terminar(),master.switch_frame(PageT2) ])
        bscpf.grid(row=5, column=3, padx=10, pady=10)

        #titulos graficas
        tlabe= Label(self, text="Señal EEG en Bruto", fg="black", font=(10))
        tlabe.grid(row=0, column=1, padx=10, pady=10)

        tlabe1= Label(self, text="Potencia Espectral de la Señal", fg="black", font=(10))
        tlabe1.grid(row=0, column=3, padx=10, pady=10)

        tlabe2= Label(self, text="Protocolo SMR", fg="black", font=(10))
        tlabe2.grid(row=2, column=1, padx=10, pady=10)

        tlabe2= Label(self, text="Histrograma de ritmos EEG", fg="black", font=(10))
        tlabe2.grid(row=2, column=3, padx=10, pady=10)

        #indicativo lados

        ttlabe= Label(self, text="[uV]", fg="black", font=(10))
        ttlabe.grid(row=1, column=0, padx=10, pady=10)

        ttlabe1= Label(self, text="[uV*2/Hz]", fg="black", font=(10))
        ttlabe1.grid(row=1, column=2, padx=10, pady=10)

        ttlabe2= Label(self, text="[uV*2/Hz]", fg="black", font=(10))
        ttlabe2.grid(row=3, column=0, padx=10, pady=10)

        ttlabe2= Label(self, text="[uV*2/Hz]", fg="black", font=(10))
        ttlabe2.grid(row=3, column=2, padx=10, pady=10)
        
        #Indicativo criterio
        ttlabe22= Label(self, text="Marcador de atencion", fg="black", font=(10))
        ttlabe22.grid(row=1, column=4, padx=10, pady=10, sticky="s")

        ttlabe22= Label(self, text="", fg="black", font=(10))
        ttlabe22.grid(row=2, column=4, padx=10, pady=10)
        
#+++++++++++++++++++++++++++++++++++++++++++++++-------------Protocolo tbr----------------------------+++++++++++++++++++++++++++++++
class Pagetbr(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

#VARIABLES Y DEFINICION DE PARAMETROS DE BRAINFLOW
        global board
        params = BrainFlowInputParams ()
        params.serial_port = ""
        board = BoardShim (BoardIds.SYNTHETIC_BOARD.value, params)
        board.prepare_session ()
        board.start_stream ()
        #variable para reiniciar
        self._job = None     
        ecg = []
        n = 200 #sfreq
        d=None
        f = open ('ud.txt','r')
        dcb = str(f.read())
        f.close()
        f = open ('sesion.txt','r')
        y=str(f.read())
        f.close()
#-----------------------------------SE PONEN GRAFICAS
        #---------SE OBTIENE SEÑAL EEG
        df = get_data(n)
        ecg.extend(df.iloc[:,0].values)
        #grafica EEG        
        f = plt.figure(figsize=(5,3), dpi=100)
        a = f.add_subplot(111)
        a.plot(ecg)
        dataPlot = FigureCanvasTkAgg(f, master=self)      
        dataPlot.get_tk_widget().grid(row=1, column=1,padx=15, pady=10, sticky="nsew")
        dataPlot.draw()
        
        #-------------transformacion de la señal EEG
        f, Pxx_den = signal.periodogram(ecg, 200)
        #grafica psd
        fr = plt.figure(figsize=(5,3), dpi=100)
        ar = fr.add_subplot(111)
        ar.plot(f, Pxx_den)
        dataPlot1 = FigureCanvasTkAgg(fr, master=self)      
        dataPlot1.get_tk_widget().grid(row=1, column=3, padx=15, pady=10, sticky="nsew")
        dataPlot1.draw()
        
        #-----------se obtiene las diferentes bandas
        deltap=sumalista(Pxx_den[1:4])
        thetap=sumalista(Pxx_den[5:7])
        alfap=sumalista(Pxx_den[8:12])
        betap=sumalista(Pxx_den[13:30])
        bandas=deltap, thetap, alfap, betap
        bandasname="Delta","Theta","Alfa","Beta"
        #grafica bandas
        fr1 = plt.figure(figsize=(5,3), dpi=100)
        ar1 = fr1.add_subplot(111)
        ar1.bar(bandasname, bandas)
        dataPlot2 = FigureCanvasTkAgg(fr1, master=self)      
        dataPlot2.get_tk_widget().grid(row=3, column=3, padx=15, pady=10, sticky="nsew")
        dataPlot2.draw()
        
        #---------------se obtiene scp
        SCPP=thetap/betap
        #grafica scp
        Pro="TBR"
        fr2 = plt.figure(figsize=(5,3), dpi=100)
        ar2 = fr2.add_subplot(111)
        ar2.bar(Pro, SCPP)
        dataPlot3 = FigureCanvasTkAgg(fr2, master=self)      
        dataPlot3.get_tk_widget().grid(row=3, column=1, padx=15, pady=10, sticky="nsew")
        dataPlot3.draw()

#---------------------------------------------------------------actualizar grafica
        def actuliazar():
            #eeg
            df = get_data(n)
            ecg.extend(df.iloc[:,0].values)
            ecgc=ecg[len(ecg)-200:len(ecg)+200]      
            a.clear()
            a.plot(ecgc)
            dataPlot.draw()
            #filtro notcj de 60hz
            samp_freq = 200  
            notch_freq = 60.0  
            quality_factor = 30.0  
            b_notch, a_notch = signal.iirnotch(notch_freq, quality_factor, samp_freq)
            ecgc = signal.filtfilt(b_notch, a_notch, ecgc)
            #filtro pasabanda
            bt, zt = butter_bandpass(1, 50, 200, order=1)
            ecgc = lfilter(bt, zt, ecgc) 

            #PSD
            f, Pxx_den = signal.periodogram(ecgc, 200)
            ar.clear()
            ar.plot(f,Pxx_den)
            dataPlot1.draw()
            #Bandas
            deltap=sumalista(Pxx_den[1:4])
            thetap=sumalista(Pxx_den[5:7])
            alfap=sumalista(Pxx_den[8:12])
            betap=sumalista(Pxx_den[13:30])
            bandas=deltap, thetap, alfap, betap
            bandasname="Delta","Theta","Alfa","Beta"
            ar1.clear()
            ar1.bar(bandasname, bandas)
            dataPlot2.draw()
            #SCP
            SCPP=thetap/betap
            Pro="TBR" 
            ar2.clear()
            ar2.bar(Pro, SCPP)
            dataPlot3.draw()
            if SCPP<=2:
                ttlabe22['text'] = "Concetrado"
                f = open ("estado.txt",'w')
                f.write("%s," % "Concentrado")
                f.write( str(SCPP))
                f.close()
            else:
                ttlabe22['text'] = "Desconcetrado"
                f = open ("estado.txt",'w')
                f.write("%s," % "Desconcentrado")
                f.write( str(SCPP))
                f.close()
            #guarda scp
            ddd="\sesion"+y+".txt"
            ubi=dcb+ddd
            f = open (ubi,'a')
            f.write("%s," % SCPP)
            f.close()

            #hace el bucle
            self._job = bscpp.after(1000, actuliazar)

        #-------funcion de parar el programa    
        def Parar():
            if self._job is not None:
                bscpp.after_cancel(self._job)
                self._job = None
        
        #------funcion de terminar
        def terminar():
            if self._job is not None:
                bscpp.after_cancel(self._job)
                self._job = None
            #guarda total de señal eeg
            d="\sesioneeg"+y+".txt"
            ubi=dcb+d
            with open(ubi, 'w') as temp_file:
                for item in ecg:
                    temp_file.write("%s\n" % item)
            #guarda promedio de protocolo en datos
            d=dcb+"\sesion"+y+".txt"
            f = open (d,'r')
            pp=f.read()
            f.close()            
            s=len(pp)
            prome=(sumalista(Pxx_den[13:30])/s)
            proto="TBR"
            f = open ("puntaje.txt",'r')
            pun=f.read()
            f.close() 
            f = open ("totalj.txt",'r')
            totalj=f.read()
            f.close() 
            punt=pun+"/"+totalj
            ubi=dcb+"\datos.txt"
            f = open (ubi,'a')
            f.write("%s\n" % y)
            f.write("%s\n" % prome)
            f.write("%s\n" % proto)
            f.write("%s\n" % punt)
            f.close()
            
        #botones interfaz
        bscpi=Button(self, text='Inicio', height = 4, width = 20, command=lambda:actuliazar())
        bscpi.grid(row=5, column=0, padx=10, pady=10)
    
        bscpp=Button(self, text='Pausar', height = 4, width = 20, command=lambda:Parar() )
        bscpp.grid(row=5, column=1, padx=10, pady=10)

        bscpf=Button(self, text='Terminar', height = 4, width = 20, command=lambda:[terminar(),master.switch_frame(PageT2) ])
        bscpf.grid(row=5, column=3, padx=10, pady=10)

        #titulos graficas
        tlabe= Label(self, text="Señal EEG en Bruto", fg="black", font=(10))
        tlabe.grid(row=0, column=1, padx=10, pady=10)

        tlabe1= Label(self, text="Potencia Espectral de la Señal", fg="black", font=(10))
        tlabe1.grid(row=0, column=3, padx=10, pady=10)

        tlabe2= Label(self, text="Protocolo TBR", fg="black", font=(10))
        tlabe2.grid(row=2, column=1, padx=10, pady=10)

        tlabe2= Label(self, text="Histrograma de ritmos EEG", fg="black", font=(10))
        tlabe2.grid(row=2, column=3, padx=10, pady=10)

        #indicativo lados

        ttlabe= Label(self, text="[uV]", fg="black", font=(10))
        ttlabe.grid(row=1, column=0, padx=10, pady=10)

        ttlabe1= Label(self, text="[uV*2/Hz]", fg="black", font=(10))
        ttlabe1.grid(row=1, column=2, padx=10, pady=10)

        ttlabe2= Label(self, text="[uV*2/Hz]", fg="black", font=(10))
        ttlabe2.grid(row=3, column=0, padx=10, pady=10)

        ttlabe2= Label(self, text="[uV*2/Hz]", fg="black", font=(10))
        ttlabe2.grid(row=3, column=2, padx=10, pady=10)

        #Indicativo criterio
        ttlabe22= Label(self, text="Marcador de atencion", fg="black", font=(10))
        ttlabe22.grid(row=1, column=4, padx=10, pady=10, sticky="s")

        ttlabe22= Label(self, text="", fg="black", font=(10))
        ttlabe22.grid(row=2, column=4, padx=10, pady=10)

#+++++++++++++++++++++++++++++++++++++++++++++++-------------Protocolo scp----------------------------+++++++++++++++++++++++++++++++
class Pagescp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        #VARIABLES Y DEFINICION DE PARAMETROS DE BRAINFLOW
        global board
        params = BrainFlowInputParams ()
        params.serial_port = ""
        board = BoardShim (BoardIds.SYNTHETIC_BOARD.value, params)
        board.prepare_session ()
        board.start_stream ()
        #variable para reiniciar
        self._job = None     
        ecg = []
        n = 200 #sfreq
        d=None
        f = open ('ud.txt','r')
        dcb = str(f.read())
        f.close()
        f = open ('sesion.txt','r')
        y=str(f.read())
        f.close()
#-----------------------------------SE PONEN GRAFICAS
        #---------SE OBTIENE SEÑAL EEG
        df = get_data(n)
        ecg.extend(df.iloc[:,0].values)
        #grafica EEG        
        f = plt.figure(figsize=(5,3), dpi=100)
        a = f.add_subplot(111)
        a.plot(ecg)
        dataPlot = FigureCanvasTkAgg(f, master=self)      
        dataPlot.get_tk_widget().grid(row=1, column=1,padx=15, pady=10, sticky="nsew")
        dataPlot.draw()
        
        #-------------transformacion de la señal EEG
        f, Pxx_den = signal.periodogram(ecg, 200)
        #grafica psd
        fr = plt.figure(figsize=(5,3), dpi=100)
        ar = fr.add_subplot(111)
        ar.plot(f, Pxx_den)
        dataPlot1 = FigureCanvasTkAgg(fr, master=self)      
        dataPlot1.get_tk_widget().grid(row=1, column=3, padx=15, pady=10, sticky="nsew")
        dataPlot1.draw()
        
        #-----------se obtiene las diferentes bandas
        deltap=sumalista(Pxx_den[1:4])
        thetap=sumalista(Pxx_den[5:7])
        alfap=sumalista(Pxx_den[8:12])
        betap=sumalista(Pxx_den[13:30])
        bandas=deltap, thetap, alfap, betap
        bandasname="Delta","Theta","Alfa","Beta"
        #grafica bandas
        fr1 = plt.figure(figsize=(5,3), dpi=100)
        ar1 = fr1.add_subplot(111)
        ar1.bar(bandasname, bandas)
        dataPlot2 = FigureCanvasTkAgg(fr1, master=self)      
        dataPlot2.get_tk_widget().grid(row=3, column=3, padx=15, pady=10, sticky="nsew")
        dataPlot2.draw()
        
        #---------------se obtiene scp
        SCPP=sumalista(Pxx_den[12:15])
        #grafica scp
        Pro="SMR"
        fr2 = plt.figure(figsize=(5,3), dpi=100)
        ar2 = fr2.add_subplot(111)
        ar2.bar(Pro, SCPP)
        dataPlot3 = FigureCanvasTkAgg(fr2, master=self)      
        dataPlot3.get_tk_widget().grid(row=3, column=1, padx=15, pady=10, sticky="nsew")
        dataPlot3.draw()

#---------------------------------------------------------------actualizar grafica
        def actuliazar():
            #eeg
            df = get_data(n)
            ecg.extend(df.iloc[:,0].values)
            ecgc=ecg[len(ecg)-200:len(ecg)+200] 

            #filtro notcj de 60hz
            samp_freq = 200  
            notch_freq = 60.0  
            quality_factor = 30.0  
            b_notch, a_notch = signal.iirnotch(notch_freq, quality_factor, samp_freq)
            ecgc = signal.filtfilt(b_notch, a_notch, ecgc)
            #filtro pasabanda
            bt, zt = butter_bandpass(0.5, 50, 200, order=4)
            ecgc = lfilter(bt, zt, ecgc) 

            a.clear()
            a.plot(ecgc)
            dataPlot.draw()

            #PSD
            f, Pxx_den = signal.periodogram(ecgc, 200)
            ar.clear()
            ar.plot(f,Pxx_den)
            dataPlot1.draw()
            #Bandas
            deltap=sumalista(Pxx_den[1:4])
            thetap=sumalista(Pxx_den[5:7])
            alfap=sumalista(Pxx_den[8:12])
            betap=sumalista(Pxx_den[13:30])
            bandas=deltap, thetap, alfap, betap
            bandasname="Delta","Theta","Alfa","Beta"
            ar1.clear()
            ar1.bar(bandasname, bandas)
            dataPlot2.draw()
            #SCP


            bt, zt = butter_bandpass(0.5, 2, 200, order=4)
            y21 = lfilter(bt, zt, ecgc)



            pos_count, neg_count = 0, 0
  
            for num in y21: 
    
                if num >= 0: 
                    pos_count += 1
                else: 
                    neg_count += 1
            
            SCPP=(neg_count/200)*100
            Pro="SMR" 
            ar2.clear()
            ar2.bar(Pro, SCPP)
            dataPlot3.draw()
            if SCPP>=45 and SCPP<=55:
                ttlabe22['text'] = "Concetrado"
                f = open ("estado.txt",'w')
                f.write("%s," % "Concetrado")
                f.write( str(SCPP))
                f.close()
            else:
                ttlabe22['text'] = "Desconcetrado"
                f = open ("estado.txt",'w')
                f.write("%s," % "Desconcentrado")
                f.write( str(SCPP))
                f.close()
            #guarda scp
            ddd=dcb+"\sesion"+y+".txt"
            
            f = open (ddd,'a')
            f.write("%s," % SCPP)
            f.close()

            #hace el bucle
            self._job = bscpp.after(1000, actuliazar)

        #-------funcion de parar el programa    
        def Parar():
            if self._job is not None:
                bscpp.after_cancel(self._job)
                self._job = None
        
        #------funcion de terminar
        def terminar():
            if self._job is not None:
                bscpp.after_cancel(self._job)
                self._job = None
            #guarda total de señal eeg
            d="\sesioneeg"+y+".txt"
            ubi=dcb+d
            with open(ubi, 'w') as temp_file:
                for item in ecg:
                    temp_file.write("%s\n" % item)
            #guarda promedio de protocolo en datos
            d=dcb+"\sesion"+y+".txt"
            f = open (d,'r')
            pp=f.read()
            f.close()            
            s=len(pp)
            prome=(sumalista(Pxx_den[13:30])/s)
            proto="SCP"
            f = open ("puntaje.txt",'r')
            pun=f.read()
            f.close() 
            f = open ("totalj.txt",'r')
            totalj=f.read()
            f.close() 
            punt=pun+"/"+totalj
            ubi=dcb+"\datos.txt"
            f = open (ubi,'a')
            f.write("%s\n" % y)
            f.write("%s\n" % prome)
            f.write("%s\n" % proto)
            f.write("%s\n" % punt)
            f.close()
            
        #botones interfaz
        bscpi=Button(self, text='Inicio', height = 4, width = 20, command=lambda:actuliazar())
        bscpi.grid(row=5, column=0, padx=10, pady=10)
    
        bscpp=Button(self, text='Pausar', height = 4, width = 20, command=lambda:Parar() )
        bscpp.grid(row=5, column=1, padx=10, pady=10)

        bscpf=Button(self, text='Terminar', height = 4, width = 20, command=lambda:[terminar(),master.switch_frame(PageT2) ])
        bscpf.grid(row=5, column=3, padx=10, pady=10)

        #titulos graficas
        tlabe= Label(self, text="Señal EEG en Bruto", fg="black", font=(10))
        tlabe.grid(row=0, column=1, padx=10, pady=10)

        tlabe1= Label(self, text="Potencia Espectral de la Señal", fg="black", font=(10))
        tlabe1.grid(row=0, column=3, padx=10, pady=10)

        tlabe2= Label(self, text="Protocolo SMR", fg="black", font=(10))
        tlabe2.grid(row=2, column=1, padx=10, pady=10)

        tlabe2= Label(self, text="Histrograma de ritmos EEG", fg="black", font=(10))
        tlabe2.grid(row=2, column=3, padx=10, pady=10)

        #indicativo lados

        ttlabe= Label(self, text="[uV]", fg="black", font=(10))
        ttlabe.grid(row=1, column=0, padx=10, pady=10)

        ttlabe1= Label(self, text="[uV*2/Hz]", fg="black", font=(10))
        ttlabe1.grid(row=1, column=2, padx=10, pady=10)

        ttlabe2= Label(self, text="[uV*2/Hz]", fg="black", font=(10))
        ttlabe2.grid(row=3, column=0, padx=10, pady=10)

        ttlabe2= Label(self, text="[uV*2/Hz]", fg="black", font=(10))
        ttlabe2.grid(row=3, column=2, padx=10, pady=10)
        
        #Indicativo criterio
        ttlabe22= Label(self, text="Marcador de atencion", fg="black", font=(10))
        ttlabe22.grid(row=1, column=4, padx=10, pady=10, sticky="s")

        ttlabe22= Label(self, text="", fg="black", font=(10))
        ttlabe22.grid(row=2, column=4, padx=10, pady=10)


#-------------------------------------muestra datos de usario buscado----------------------------------------------------------------
class PageT2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        f = open ('ud.txt','r')
        dcb = str(f.read())
        f.close()
        d="\datos.txt"
        ubi=dcb+d
        #realiza tabla y lo muestra en gui
        i=0
        j=0
        archi1=open(ubi,"r")
        for linea in archi1:

            tabla= Label(self, text=linea, height=2, width=15, bg='white', fg="black", font=(10))
            tabla.grid(row=i, column=j, padx=10, pady=10, sticky="e")
            j+=1
            if j==4:
                i+=1
                j=0
       
        def finalizar():
            f = open ('nivel.txt','w')
            f.write(str(0))
            f.close()
            self.master.destroy()

        mdb=Button(self, text='Finalizar', command=lambda:finalizar())
        mdb.grid(row=i+1, column=1, padx=10, pady=10, sticky="e", columnspan=2)



if __name__ == "__main__":
    app = SampleApp()
    
    app.mainloop()