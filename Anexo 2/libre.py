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



def butterBandPassFilter(lowcut, highcut, samplerate, order):
    "Generar filtro de paso de banda Butterworth"
    semiSampleRate = samplerate*0.5
    low = lowcut / semiSampleRate
    high = highcut / semiSampleRate
    b,a = signal.butter(order,[low,high],btype='bandpass')
    print("bandpass:","b.shape:",b.shape,"a.shape:",a.shape,"order=",order)
    print("b=",b)
    print("a=",a)
    return b,a

def butterBandStopFilter(lowcut, highcut, samplerate, order):
    "Generar filtro de parada de banda de Butterworth"
    semiSampleRate = samplerate*0.5
    low = lowcut / semiSampleRate
    high = highcut / semiSampleRate
    b,a = signal.butter(order,[low,high],btype='bandstop')
    print("bandstop:","b.shape:",b.shape,"a.shape:",a.shape,"order=",order)
    print("b=",b)
    print("a=",a)
    return b,a

iSampleRate = 2000	#Frecuencia de muestreo

plt.figure(figsize=(12,5))
ax0 = plt.subplot(121)
for k in [2, 3, 4]:
    b, a = butterBandPassFilter(3,70,samplerate=iSampleRate,order=k)
    w, h = signal.freqz(b, a, worN=2000)
    ax0.plot((iSampleRate*0.5/np.pi)*w,np.abs(h),label="order = %d" % k)

ax1 = plt.subplot(122)
for k in [2, 3, 4]:
    b, a = butterBandStopFilter(48, 52, samplerate=iSampleRate, order=k)
    w, h = signal.freqz(b, a, worN=2000)
    ax1.plot((iSampleRate*0.5/np.pi)*w,np.abs(h),label="order = %d" % k)