"""
 @details:  Confeccionar una aplicación que permita ingresar un entero por teclado y 
            al presionar un botón muestre dicho valor elevado al cuadrado en una Label. 
"""

from tkinter import *



class Aplicacion:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Entry")

        self.lbl_mensaje = Label(self.ventana, text = "ingrese un número:")
        self.lbl_mensaje.grid(column = 0 , row = 0)

        self.dato = StringVar()
        self.etr_entrada = Entry(self.ventana, width = 25, textvariable = self.dato , justify = "center")
        self.etr_entrada.grid(column = 1, row = 0)

        self.btn_boton1 = Button(
                                    self.ventana, 
                                    text = "calcular cuadrado del numero ingresado", 
                                    command = self.calcularCuadrado
                                )
        self.btn_boton1.grid(column = 0, row = 1)

        self.lbl_resultado = Label(self.ventana, text = "-")
        self.lbl_resultado.grid(column = 1, row = 1)

        self.ventana.mainloop()


    def calcularCuadrado(self):
        valorDeEntrada = int(self.etr_entrada.get())
        resultado = valorDeEntrada * valorDeEntrada
        self.lbl_resultado.config(text= resultado)

app = Aplicacion()