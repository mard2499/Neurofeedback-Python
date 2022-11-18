import pygame
from pygame.locals import *
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
from random import choice

pygame.init()

joystick = pygame.joystick.Joystick(0)


#variables introducidas
dp=str(0)
f = open ('puntaje.txt','w')
f.write(dp)
f.close()
f = open ('totalj.txt','w')
f.write(dp)
f.close()
cap = cv2.VideoCapture('solovr.mp4')
cae=0
tiemp=0
com=0
puntajes=0
conte=0
zt="Puntaje"
totalj=0
f = open ('nivel.txt','r')
nivj=f.read()
f.close()


if nivj==1:
    nivj=6
if nivj==2:
    nivj=4
if nivj==3:
    nivj=2

def finalizar():
    global cap
    cap.release()

def elegir_visualizar_video():
    
    global cap
    global cae
    global com
    global totalj
    if cap is not None:
        lblVideo.image = ""
        cap.release()
        cap = None
    
        opciones = [1,1,2,2,3,4,5]
        aleatorio= choice(opciones)

            
        if aleatorio==1:
            cap= cv2.VideoCapture('arbolcaevr.mp4')
            cae=1
            com=0
            totalj=1
            f = open ('totalj.txt','w')
            f.write(str(totalj))
            f.close()
            visualizar()
        if aleatorio==2:
            cap= cv2.VideoCapture('perropasavr.mp4')
            totalj=1
            f = open ('totalj.txt','w')
            f.write(str(totalj))
            f.close()
            cae=1
            com=0
            visualizar()
        if aleatorio==3: 
            cap= cv2.VideoCapture('arbolquieto.mp4')
            cae=0
            com=0
            visualizar()
        if aleatorio==4: 
            cap= cv2.VideoCapture('perroquietovr.mp4')
            cae=0
            com=0
            visualizar()
        if aleatorio==5:     
            cap = cv2.VideoCapture('solovr.mp4') 
            cae=0  
            com=0
            visualizar()         


def visualizar():
    global cap
    global cae
    global tiemp
    global com
    global zt
    global conte
    global nivj
    global totalj
    if cap is not None:
        
        ret, frame = cap.read()
        if ret == True:
            
            frame = imutils.resize(frame, width=1150, height=500)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            lblVideo.configure(image=img)
            lblVideo.image = img
            
            if pygame.event.get():
                if cae==1 and com==0:
                    if joystick.get_button(0) and  tiemp>40 and tiemp<80:
                        f = open ('puntaje.txt','r')
                        puntajes=int(f.read())
                        f.close()
                        puntajes=puntajes+1
                        f = open ('puntaje.txt','w')
                        f.write(str(puntajes))
                        f.close()
                        zt="Puntaje:"+str(puntajes)

                        com=1 
                        lblInfo1.config(text=zt, bg="green" ) 

                    else:
                        lblInfo1.config(text=zt, bg="red" )
                        com=1         

        
            tiemp+=1

            if tiemp>80 and com==0 and cae==1:
                lblInfo1.config(text=zt, bg="red" )

            conte+=1
            if conte==40:
                f = open ('estado.txt','r')
                estado=f.read().split(sep=',')
                f.close()
                dpr=str(estado[0])
                if dpr =="Concetrado":
                    deci="Estado: "+dpr
                    lblInfoVideoPath.config(text=deci, bg="green" )
                    conte=0
                if dpr=="Desconcentrado":
                    deci="Estado: "+dpr
                    
                    lblInfoVideoPath.config(text=deci, bg="red" )
                    conte=0
                
            
            lblVideo.after(nivj, visualizar)
        
        else:
            cap.release()
            opciones = [1,1,2,2,3,4,5]
            aleatorio= choice(opciones)

                
            if aleatorio==1:
                cap= cv2.VideoCapture('arbolcaevr.mp4')
                lblInfo1.config(text=zt, bg="white" )
                tiemp=0
                cae=1
                com=0
                totalj+=1
                f = open ('totalj.txt','w')
                f.write(str(totalj))
                f.close()
                visualizar()
            if aleatorio==2:
                cap= cv2.VideoCapture('perropasavr.mp4')
                lblInfo1.config(text=zt, bg="white" )
                tiemp=0
                cae=1
                com=0
                totalj+=1
                f = open ('totalj.txt','w')
                f.write(str(totalj))
                f.close()
                visualizar()
            if aleatorio==3: 
                cap= cv2.VideoCapture('arbolquieto.mp4')
                lblInfo1.config(text=zt, bg="white" )
                tiemp=0
                cae=0
                com=0
                visualizar()
            if aleatorio==4: 
                cap= cv2.VideoCapture('perroquietovr.mp4')
                lblInfo1.config(text=zt, bg="white" )
                tiemp=0
                cae=0
                com=0
                visualizar()
            if aleatorio==5:     
                cap = cv2.VideoCapture('solovr.mp4')
                lblInfo1.config(text=zt, bg="white" )
                tiemp=0
                cae=0
                com=0  
                visualizar() 
                
                
            
                
      



root = Tk()
btnVisualizar = Button(root, text="Iniciar Juego", command=elegir_visualizar_video)
btnVisualizar.grid(column=0, row=0, padx=5, pady=5, columnspan=2)

def callback(event):
    
    funcion()
    
def funcion():   
    global com
    global cae
    global tiemp
    global zt
    if cae==1 and com==0:
               

        if tiemp>40 and tiemp<80:
            f = open ('puntaje.txt','r')
            puntajes=int(f.read())
            f.close()
            puntajes=puntajes+1
            f = open ('puntaje.txt','w')
            f.write(str(puntajes))
            f.close()
            zt="Puntaje:"+str(puntajes)
            
            com=1 
            lblInfo1.config(text=zt, bg="green" ) 
        

        else:
            lblInfo1.config(text=zt, bg="red" )
            com=1 




lblInfo1 = Label(root, text="Puntaje:")
lblInfo1.grid(column=0, row=1)
lblInfoVideoPath = Label(root, text="Estado:")
lblInfoVideoPath.grid(column=1, row=1)
lblVideo = Label(root)
lblVideo.grid(column=0, row=2, columnspan=2)


root.bind('<Return>', callback)

root.mainloop()
           