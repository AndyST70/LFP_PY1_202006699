from cgitb import text
from pickle import GLOBAL
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
from tkinter import filedialog, Tk
import sys
from tkinter.scrolledtext import ScrolledText
from analizador import AnalizadorLexico
lexico = AnalizadorLexico ()

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


    boton_analizar = Button(ventana, text  = "Analizar", command = analizar, width="30", height="2", bg = "#00FF58" )
    boton_analizar.place(x=22, y =450)
    
    boton_cargar = Button(ventana, text = "Cargar", command= abrir, width= "30", height= "2", bg = "#00FF58" )
    boton_cargar.place(x= 350, y = 450)

    lista_ = combo = ttk.Combobox()
    lista_.place(x= 100, y = 50)
    combo.place(x=500, y=75)

    global caja_texto

    caja_texto = ScrolledText(ventana, width = "50", height= "20")
    caja_texto.place(x=40, y = 60)
    


    #? utilizamos nuestro pack layout manager
    #? uso del boton de la ventana
    #boton_1.grid(row = 1, column=0, sticky="SE")
    #! advertencia: este metodo debe ser el último
    
    
    entrada.pack()
    ventana.mainloop()



def analizar():
   #!traemos nuestros datos para manipulación y realización de tablas 
   a = caja_texto.get("1.0", tk.END)
   lexico.iniciar()
   lexico.Analizar(a)
   lexico.imprimirTokens()
   lexico.imprimirErrores()
   

    # modificamos el boton al tocarlo
   #boton_1.config(text = "Ingresando") 
    #!creación de botones 
#boton_1 = ttk.Button(ventana, text = "valor", command= evento_click)




def abrir():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Seleccionar un archivo",
        initialdir = "./",
        filetypes = [
            #Definimos los tipo de archivo
            ("archivos .form", "*.form"),
            ("todos los archivos",  "*.*")
        ]
    )
    #si no se seleccióno ningun archivo
    if archivo is None:
        print('No se selecciono ningun archivo\n')
        return None
    else:
        archivo_2 = open(archivo.name, "r", encoding = "utf-8")
        #Leer el texto
        texto = archivo_2.read()
        archivo_2.close()
        caja_texto.delete("1.0", "end")
        caja_texto.insert(INSERT, texto)
        return texto #retorna nuestro texto

def salir():
    sys.exit()
    
if __name__ == '__main__':
   
    archivo_prueba = '''Hola mundo ~>> [
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
    >
]'''
    ventana_creacion()
    # lexico.Analizar(txt)
    # for token in lexico.ListaTokens:
    #     print(len(token.))
    # for token in lexico.ListaErrores:
    #     print(len(lexico.error_append()))
    

    print(len(lexico.ListaTokens))
    print(len(lexico.ListaErrores))