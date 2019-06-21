import tkinter as tk
"""
ventana =  tk.Tk()
ventana.title('Hola Christian')
ventana.mainloop()
"""

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('hola sistemas de información geográfica')
        self.ventana.mainloop()


app = Aplicacion()