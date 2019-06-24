import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb 
from tkinter import scrolledtext as st  
import articulos

class FormularioArticulos:

    def __init__(self):
        self.articulo1 = articulos.Articulos()
        self.ventana1 = tk.Tk()
        self.ventana1.title("Mantenimiento de artículos")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.carga_articulos_view()
        self.consultar_por_codigo_view()
        self.listado_completo_view()
        self.eliminar_articulo_view()

        self.cuaderno1.grid(column = 0 , row = 0 , padx = 10, pady = 10)
        self.ventana1.mainloop()

    def carga_articulos_view(self):
        self.pagina1 = ttk.Frame(self.cuaderno1) # vincula contenido con la pestaña
        self.cuaderno1.add(self.pagina1, text = "Carga de articulos") # agrega a la pestaña 1 el frame pagina 1 y el titulo de la pestaña "carga articulios"
        
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text = "Articulo")
        self.labelframe1.grid(column = 0, row = 0, padx = 5, pady = 10)
        
        self.label1 = ttk.Label(self.labelframe1, text = "Descripción:")
        self.label1.grid(column=0 , row = 0, padx = 4, pady = 4)
        self.descripcioncarga = tk.StringVar()
        self.entrydescripcion = ttk.Entry(self.labelframe1, textvariable = self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)

        
        self.label2=ttk.Label(self.labelframe1, text="Precio:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.preciocarga=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        datos=(self.descripcioncarga.get(), self.preciocarga.get())
        self.articulo1.agregar(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.descripcioncarga.set("")
        self.preciocarga.set("")


    def consultar_por_codigo_view(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text = "Consultar por código")

        self.labelframe1 = ttk.LabelFrame(self.pagina2, text = "Artículo")
        self.labelframe1.grid(column = 0, row = 0, padx = 5, pady = 10)
        
        self.label1 = ttk.Label(self.labelframe1, text = "Código:")
        self.label1.grid(column = 0, row = 1, padx = 4, pady = 4)
        self.codigocarga = tk.StringVar()
        self.entrycodigo = ttk.Entry(self.labelframe1, textvariable = self.codigocarga)
        self.entrycodigo.grid(column = 1, row = 1, padx = 4 , pady = 4)
        
        self.label2 = ttk.Label(self.labelframe1, text = "Descripción:")
        self.label2.grid(column = 0, row = 3, padx = 4, pady = 4)
        self.descripcioncarga = tk.StringVar()
        self.entrydescripcion = ttk.Entry(self.labelframe1, textvariable = self.descripcioncarga, state = "readonly")
        self.entrydescripcion.grid(column = 1, row = 3, padx = 4 , pady = 4)

        self.label3 = ttk.Label(self.labelframe1, text = "Precio:")
        self.label3.grid(column = 0, row = 4, padx = 4, pady = 4)
        self.preciocarga = tk.StringVar()
        self.entryprecio = ttk.Entry(self.labelframe1, textvariable = self.preciocarga, state = "readonly")
        self.entryprecio.grid(column = 1, row = 4, padx = 4 , pady = 4)

        self.botonEnviar = ttk.Button(self.labelframe1, text = "Consultar", command = self.consultar)
        self.botonEnviar.grid(column = 2, row = 5 , padx = 3 , pady = 3 )

    def consultar(self):
        idLeido = (self.codigocarga.get(),)
        articulo = self.articulo1.buscarArticuloPorId(idLeido)
        if articulo != None:
            self.descripcioncarga.set(articulo[0]) 
            self.preciocarga.set(articulo[1])
        else:
            self.descripcioncarga.set("")
            self.preciocarga.set("")
            mb.showinfo("Informacion","No existe un artículo con el código ingresado")

    def listado_completo_view(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text = "Listado Completo")

        self.labelframe1 = ttk.LabelFrame(self.pagina3, text = "Todos los Articulos")
        self.labelframe1.grid(column = 0 , row = 0 , padx = 5, pady = 10)
        self.boton1 = ttk.Button(self.labelframe1, text = "Listado completo", command = self.listar)
        self.boton1.grid(column = 0 , row = 0, padx = 4, pady = 4)

        self.scrolledtext1 = st.ScrolledText(self.labelframe1, width = 30, height = 10)
        self.scrolledtext1.grid(column = 0, row = 1, padx = 10 , pady = 10)

    def listar(self):
        tabla = self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)
        for fila in tabla:
            self.scrolledtext1.insert(tk.END, "codigo:" + str(fila[0]) + "\n descripción:" + fila[1] + "\n precio:" + str(fila[2])+"\n\n")


    def eliminar_articulo_view(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text = "Eliminar Artículo")

        self.labelFrame1 = ttk.LabelFrame(self.pagina4, text = "Eliminar por codigo de Artículo") 
        self.labelFrame1.grid(column = 0 , row = 0 ,padx = 5 , pady = 10)

        self.labelcodigo = ttk.Label(self.labelFrame1, text = "Código: ")
        self.labelcodigo.grid(column = 0 ,row = 1, padx = 3 , pady = 3)   
app = FormularioArticulos()