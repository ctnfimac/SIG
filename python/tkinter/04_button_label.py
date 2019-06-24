"""
 @details:  Mostrar los botones del 1 al 5. Cuando se presiona mostrar en una 
            Label todos los botones presionados hasta ese momento. 
"""

from tkinter import *

class Aplicacion:

    def __init__(self):
        self.valorLcd = "0"
        self.ventana = Tk()
        self.ventana.title("ejemplo 04")
        self.ventana.geometry('{}x{}'.format(180,60))

        self.addPantallas()
        self.addButtons()

        self.ventana.mainloop()


    def addPantallas(self):
        self.lbl_lcd = Label(self.ventana,text=self.valorLcd)
        self.lbl_lcd.grid(column= 0 , row = 0)
    

    def addButtons(self):
        self.btn_numero1 = Button(self.ventana, text= "1", command = self.mtd_btn1)
        self.btn_numero1.grid(column = 0 , row = 1)

        self.btn_numero2 = Button(self.ventana, text= "2", command = self.mtd_btn2)
        self.btn_numero2.grid(column = 1 , row = 1)

        self.btn_numero3 = Button(self.ventana, text= "3", command = self.mtd_btn3)
        self.btn_numero3.grid(column = 2 , row = 1)

        self.btn_numero4 = Button(self.ventana, text= "4", command = self.mtd_btn4)
        self.btn_numero4.grid(column = 3 , row = 1)

        self.btn_numero5 = Button(self.ventana, text= "5", command = self.mtd_btn5)
        self.btn_numero5.grid(column = 4 , row = 1)

    def mtd_btn1(self):
        self.valorLcd = self.valorLcd + "1"
        self.lbl_lcd.config(text = self.valorLcd)

    def mtd_btn2(self):
        self.valorLcd = self.valorLcd + "2"
        self.lbl_lcd.config(text = self.valorLcd)

    def mtd_btn3(self):
        self.valorLcd = self.valorLcd + "3"
        self.lbl_lcd.config(text = self.valorLcd)

    def mtd_btn4(self):
        self.valorLcd = self.valorLcd + "4"
        self.lbl_lcd.config(text = self.valorLcd)

    def mtd_btn5(self):
        self.valorLcd = self.valorLcd + "5"
        self.lbl_lcd.config(text = self.valorLcd)

app = Aplicacion()