import tkinter as tk
import os as uso_
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfile
from tkinter import filedialog, Tk
import sys
from tkinter.scrolledtext import ScrolledText
from analizador import AnalizadorLexico
import webbrowser
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
    
    boton_enter = Button(ventana, text = "Enter", command = enter_entrada, width="5", height="1", bg ="#00FF58")
    boton_enter.place( x = 500, y = 150)

    boton_cargar = Button(ventana, text = "Cargar", command= abrir, width= "30", height= "2", bg = "#00FF58" )
    boton_cargar.place(x= 350, y = 450)
    global opcion_escogida
    opcion_escogida = tk.StringVar()
    global combo
    combo = ttk.Combobox( textvariable= opcion_escogida)
    combo = ttk.Combobox( values=[
                                    "Reporte de Tokens", 
                                    "Reporte de errores",
                                    "Manual Usuario",
                                    "Manual Tecnico"])
    # combo.bind("<<ComboboxSelected>>", op_uso())
    
    combo.place(x=500, y=75)
    #!===================================================
    global caja_texto

    caja_texto = ScrolledText(ventana, width = "50", height= "20")
    caja_texto.place(x=40, y = 60)
    #? utilizamos nuestro pack layout manager
    #? uso del boton de la ventana
    #boton_1.grid(row = 1, column=0, sticky="SE")
    #! advertencia: este metodo debe ser el último
    entrada.pack()
    ventana.mainloop()
# def llamadas(event):
#     if combo.get() == "Reporte de Tokens":
#         lexico.imprimirTokens()
        # if opcion != None:
        #     messagebox.showinfo("Error", "Carga tu información")

    # if opcion_escogida.get() == "Reporte de Tokens":
    #    combo.set()
    #    if formato != None
    #    analizar()
# def tenemos(codigo: str):
#     if len (codigo) > 0:
#        global datos_analic
#        datos_analic = AnalizadorLexico()
#        datos_analic.busqueda(codigo)
       
#     else:
#         pass
def analizar():
   #!traemos nuestros datos para manipulación y realización de tablas 
   a = caja_texto.get("1.0", tk.END)
   lexico.iniciar()
   lexico.Analizar(a)
   automatic()
#    lexico.imprimirTokens()
#    lexico.imprimirErrores()
   
def enter_entrada():
    #!==================================================
    if combo.get() == "Reporte de Tokens":
        combo.set("")
        if lexico.ListaTokens != None:
           lexico.imprimirTokens()
        else: 
            print("No tenemos información")

    elif combo.get() == "Reporte de errores":
        combo.set("")
        if lexico.ListaErrores != None:
            lexico.imprimirErrores()
        else: 
            print("No tenemos información")
    elif combo.get() == "Manual Usuario":
        combo.set("")
        rutars("Manual Usuario.pdf")

    elif combo.get() == "Manual Tecnico":
        combo.set("")
        rutars("Manual Tecnico.pdf")

def rutars(entrada):
    ruta_datos = uso_.path.dirname(uso_.path.abspath(__file__))+ "\\archivos\{}".format(entrada)
    webbrowser.open_new(ruta_datos)
    
    print(ruta_datos)
                    
    # selection = combo.get()
    # #? creacion de mensajes
    # messagebox.showinfo(
    # title="Nuevo elemento seleccionado",
    # message=selection)

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
    
def automatic():
    repo = open ("Reporte.html", "w", encoding="utf-8")
    genera_Automatic = ""
    genera_Automatic = '''
    <form>
    <div class="form-group"><label for="exampleInputEmail1">Nombre </label> <input id="exampleInputEmail1" class="form-control" type="email" placeholder="Ingresar Nombre" aria-describedby="emailHelp" /> <small id="emailHelp" class="form-text text-muted"></small></div>
        <p ></p>
    <div class="form-check">
        <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
        <label class="form-check-label" for="flexRadioDefault1">
            Masculino
        </label>
    </div>
    <div class="form-check">
        <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
        <label class="form-check-label" for="flexRadioDefault2">
            Femenino
        </label>
    </div>
        <p ></p>
    
    </form>
    <div class="my-1 mr-2">Pais<select id="inlineFormCustomSelect" class="custom-select mr-sm-2">

    <option selected="selected"></option>
    <option value="1">Guatemala</option>
    <option value="2">El Salvador</option>
    <option value="3">Honduras</option>
    <option value="4">Washington</option>
    </select>
    </div>
        <p ></p>
        <p ></p>
        <p><button class="btn btn-primary" type="submit">Submit</button></p>'''.format(genera_Automatic)
    repo.write(genera_Automatic)
    repo.close()
    webbrowser.open_new("Reporte.html")
    

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
    
    lexico.Tabla_tokens()
    print(len(lexico.ListaTokens))
    print(len(lexico.ListaErrores))