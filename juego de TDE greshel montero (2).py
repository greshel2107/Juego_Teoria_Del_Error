from tkinter import *
from tkinter import ttk 

#===================JUEGO COMO TAL================
def nueva ():
    
    ventana1.title("Empezemos a jugar")
    ventana1.geometry("1000x1000")
    ventana1.config(bg="#42A8A1")
    boton.destroy()
    btn2.destroy()
    ventana1.mainloop()


    #====================ACERCA DEL JUEGO ====================

def A_D_J ():
    
  
    ventana1 .title("Acerca del juego ")
    ventana1.geometry("700x700")
    ventana1.config(bg="#ECD4FF")
G
    boton.destroy()
    btn2.destroy()
    ventana1.mainloop()

#=====================VENTANA PRINCIPAL ==================

ventana1 = Tk()
color_bg="white"
ventana1.title("Welcome")
ventana1.geometry("700x700")
ventana1.config(bg="#ECD4FF")



ventana1.mainloop()

#====================BOTONES============================
boton=Button(ventana1,text="Jugar",font=("cambria",20),command = nueva)
boton.place(x=300,y=350)

btn2= Button(ventana1,text="Acerca del juego",font=("cambria",20),command = A_D_J)
btn2.place(x= 260, y =440)


