import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
from tkinter import filedialog, Tk
import sys
from analizador import AnalizadorLexico
ret = AnalizadorLexico ()
def ventana_creacion():
    #!ttk son los componentes
    #? creamo nuestro objeto 
    ventana = tk.Tk()
    #? modificamos el tamaño de la ventana
    ventana.geometry('650x550')
    #? titulo de la ventana
    ventana.title("Interfaz Gráfica")
    #? configuramos nuestro icono de nuestra app
    ventana.iconbitmap("icono.ico")
    ventana.resizable(0,0) #? evitamos que cambie de tamaño
    ventana.config(background= "#6898FD")



    #========================================================
    entrada = Label(text = "Menu",  font = ("Cambria", 14), bg= "#FFFFFF", width = "500", height = "2")
    #!           Label
    ventana.rowconfigure(0, weight=1)

    # Ingr_entrada = tkinter.Label(ventana, text = "             Bienvenido            ").pack()


    #! ===========================================
    #? creación de nuestra ventana


    boton = Button(ventana, text  = "Analizar", command = evento_click, width="30", height="2", bg = "#00FF58" )
    boton.place(x=22, y =450)

    lista_ = combo = ttk.Combobox()
    combo.place(x=500, y=75)


    #? utilizamos nuestro pack layout manager
    #? uso del boton de la ventana
    #boton_1.grid(row = 1, column=0, sticky="SE")
    #! advertencia: este metodo debe ser el último
    
    
    entrada.pack()
    ventana.mainloop()



def evento_click():
   print(" Prueba de ejecución")
    # modificamos el boton al tocarlo
   #boton_1.config(text = "Ingresando") 
    #!creación de botones 
#boton_1 = ttk.Button(ventana, text = "valor", command= evento_click)




# def abrir():
#     Tk ().withdraw()
#     archivo = askopenfile(
#         title = "ingresa tu archivo",
#         initialdir = "./",
#         filetypes = [
#             ("archivo .form", "*.form"),
#             ("todos los archivos", "*.*")
#         ]
#     )
#     dato = open(archivo, "r", encoding = "utf-8")
#     dato = ""
#     global leer_datos
#     leer_datos = dato.read()
#     dato.close()
#     return leer_datos

def salir():
    sys.exit()
    
if __name__ == '__main__':
    
    txt = '''formulario ~>> [
    <
        tipo: "etiqueta",
        valor: "Nombre:"
    >,

    <
        tipo: "texto",
        valor: "Nombre",
        fondo: "Ingrese nombre"
    >,

    <
        tipo: "grupo-radio",
        nombre: "sexo",
        valores: ['Masculino', 'Femenino']
    >,

    <
        tipo: "grupo-option",
        nombre: "país",
        valores: ['Guatemala', 'El salvador', 'Honduras']
    >,

    <
        tipo: "boton",
        valor: "Valor",
        evento: <EVENTO>
    >,
]'''
    ventana_creacion()
    ret.analizador(txt)
  