"""
 @details:  Disponer dos objetos de la clase Button con las etiquetas: 
 "varón" y "mujer", al presionarse mostrar en la barra de títulos 
 de la ventana la etiqueta del botón presionado. 
"""

#import tkinter * as tk
from tkinter import *

class Aplicacion:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("mi primer entorno gráfico")
        self.ventana.geometry('{}x{}'.format(200,50)) 
        self.addBotones()
        self.ventana.mainloop()


    def varon(self):
        self.ventana.title("Varón")


    def mujer(self):
        self.ventana.title("Mujer")

    
    def addBotones(self):
        self.boton1 = Button(self.ventana, text = "Varón", command= self.varon)
        self.boton1.grid(column = 0, row = 0)

        self.boton2 = Button(self.ventana, text = "Mujer", command = self.mujer)
        self.boton2.grid(column = 1 , row = 0)


app = Aplicacion()