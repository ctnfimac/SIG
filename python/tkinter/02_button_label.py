"""
 @details:  Mostrar una ventana y en su interior dos botones y una label. 
            La label muestra inicialmente el valor 1. Cada uno de los botones 
            permiten incrementar o decrementar en uno el contenido de la label 
"""
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.valor = 1
        self.ventana = tk.Tk()
        self.ventana.title('Controles de button y label')
        self.label = tk.Label(self.ventana, text = self.valor, justify = 'center')
        self.label.grid(column = 0, row = 0)
        self.label.configure(foreground = "red")
        
        self.boton1 = tk.Button(self.ventana, text="Incrementar", command = self.incrementar)
        self.boton1.grid(column = 0 , row = 1)

        self.boton2 = tk.Button(self.ventana, text = "Decrementar", command = self.decrementar)
        self.boton2.grid(column=1, row = 1)

        self.ventana.mainloop()


    def incrementar(self):
        self.valor = self.valor + 1 
        self.label.config(text = self.valor)

    def decrementar(self):
        self.valor = self.valor - 1
        self.label.config(text = self.valor)

app = Aplicacion()