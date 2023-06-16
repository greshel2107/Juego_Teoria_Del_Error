from tkinter import *
from tkinter import ttk 
from tkinter import PhotoImage
from functools import *
from operator import *
import random 

#======[Funciones del juego]========
def crea_matriz ():
    mat_num=[]
    for i in range (10):
        vec=[None]*10
        mat_num.append(vec)
        return mat_num

def carga_matriz(mat_num):
    for i in range (10):
        for j in range (10):
            mat_num [i][j]=random.randint(0,1)

def mat_botones(mat_num):
    mat_bot=[]
    for i in range (10):
        vec= [None]*10
        mat_bot.append(vec = random.randint(0,1))
        
    for i in range(10):
        for j in range(10):
            mat_bot[i][j]=Button (text="", command = partial(btn_click,i,j))
            mat_bot[i][j].place(x=j*30, y=i*30,width= 30 ,height=30)

def btn_click (mat_num,fil, col):
    print (mat_num[fil][col])

#======== Juego =======
def juego():
    juego=Tk()
    juego.title("juego de minas ")
    juego.geometry("400x400")
    juego.config(bg="#ECD4FF")

    juego.mainloop()

#=============ACERCA DEL JUEGO================
def A_D_J():

    V_A_D_J=Tk()
    V_A_D_J.title("informacion del juego")
    V_A_D_J.geometry("400x400")
    V_A_D_J.config(bg="#ECD4FF")

    lbl=Label(V_A_D_J, text= "Bienvenidos al Encuentra las minas ")
    lbl.pack

    print( "Bienvenidos al juego ENCUENTRA LAS MINAS ")  
    print("       este, juego consiste en que en un marco de casillas de 0 y 1 " ) 
    print("                      estan ubicadas las minas , de manera tal que ")
    print("   los 0 representan:espacios ")
    print("    los 1 representan:minas   ")
    print("              el jugador contara con un total de dos vidas")
    print("    Buena Suerte !!!")
    
    V_A_D_J.mainloop()
#===========VENTANA MENU===============
ven_menu=Tk()
ven_menu.title("Menu del juego")
ven_menu.geometry("400x400")
ven_menu.config(bg="#ECD4FF")

boton=Button(ven_menu,text="PLAY",font=("cambria",20),command = juego)
boton.place(x=300,y=350)

btn2= Button(ven_menu,text="Informacion del juego",font=("cambria",20),command = A_D_J)
btn2.place(x= 260, y =400)
    
#================JUEGO COMO TAL ================



ven_menu.mainloop()

