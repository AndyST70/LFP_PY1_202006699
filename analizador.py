
from error import Error
from Token import constructor
from prettytable import PrettyTable
import os
from tkinter import messagebox
class AnalizadorLexico():
    def __init__(self):
        self.ListaTokens = []
        self.ListaErrores = [] 
        self.linea = 1
        self.columna= 0
        self.lexema = "" # strings
        self.estado = 1  #
        self.i = 0 #? con este vamos recorriendo nuestras listas y guardando
        #tipo, lexema, linea y columna
    # while=?
    def agregar_token(self, caracter, tipo, linea, columna ):
        self.ListaTokens.append(constructor(caracter, linea, columna, tipo))
        self.lexema = ""
    def error_append(self, caracter, linea, columna,  tipo):
        self.ListaErrores.append(Error("caracter: ", caracter, "linea: ", linea, "columna: ", columna, "tipo", tipo))
    #!===========================================================
    #? Entrada de excepciones, simbolos, caracteres, opciones, etc
    def Estado0(self, caracter):
        '''Documentación q0'''                   
            # elif estado == 2: 
        if caracter.isalpha():#! is alpha se utiliza para el manejo de cadenas o bien para reconocer caracteres.
            self.lexema += caracter
            self.columna +=1
            self.estado = 1  # l, s, a, d

        elif caracter.isdigit():
            self.lexema += caracter
            self.columna +=1
            self.estado = 2

        elif caracter ==".":
            self.lexema += caracter
            self.columna += 1
            self.estado = 2


        elif caracter =="[":
            self.lexema += caracter
            self.columna += 1
            self.estado = 4

        elif caracter == "]":
            self.lexema += caracter
            self.columna += 1
            self.estado = 4
        elif caracter == "<":
            self.lexema += caracter
            self.columna += 1
            self.estado = 4

        elif caracter == ">":
            self.lexema += caracter
            self.columna += 1
            self.estado = 4
        
        elif caracter =="{":
            self.lexema += caracter
            self.columna += 1
            self.estado = 4


        elif caracter =="}":
            self.lexema += caracter
            self.columna += 1
            self.estado = 4

        elif caracter ==",":
            self.lexema += caracter
            self.columna += 1
            self.estado = 4
        
        elif caracter =="'" or caracter == '"':
            self.lexema += caracter
            self.columna +=1
            self.estado = 3
        
        elif caracter ==":":
            self.lexema += caracter
            self.columna +=1
            self.estado = 4
        
        elif caracter == "#":
            self.lexema += caracter
            self.columna += 1
            self.estado = 4

        elif  caracter == ";":
            self.lexema += caracter
            self.columna+=1
            self.estado = 4
        
        elif caracter == "\t":
            self.columna +=1

        elif caracter == " ":
            self.columna += 1

        elif caracter == '\n':
            self.linea += 1
            self.columna = 1

        elif caracter == "$":
            pass
        
        elif caracter == '\r':
            pass

        else:
            self.lexema += caracter
              #! nos dara un error
            self.ListaErrores.append(Error(self.lexema, 
            self.linea,
            self.columna,
            "Error Caracter desconocido"
            )) 
    
    #!===========================================================
    #? Estados para ingreso de cadenas, indicadores y reservadas, excepciones de cadenas
    def Estado1(self, caracter :str):
        '''Estado q1'''

        if caracter.isalpha(): # tipo
            self.lexema += caracter 
            self.columna +=1
            self.estado = 1

        elif caracter.isdigit(): #tipo2
            self.lexema +=caracter
            self.columna += 1    
            self.estado = 1
            
        elif caracter == "_": #tipo_2a
            self.estado = 1
            self.lexema +=caracter
            self.columna += 1    
        
        else:
         #!===================================================
                #? Asignamos nuestras palabras reservadas
                #? formulario, tipo, valor, fondo, nombre
                #? valores, evento
            if self.lexema == "formulario" :
                self.agregar_token(self.lexema, "palabra reservada", self.linea, self.columna)                 
                self.estado = 0
                self.i -= 1
        #!======================================================
            # elif self.lexema == "Nombre" or self.lexema =="Ingrese Nombre" or self.lexema == "Guatemala" or self.lexema == "El salvador" or self.lexema ==" Honduras":
            #     self.agregar_token(self.lexema, "Cadena, seguida de letras minusculas/numeros/espacios ", self.linea, self.columna)
            #     self.estado = 0
            #     self.i -= 1
            
            elif self.lexema == "tipo" or self.lexema == "valor" or self.lexema == "fondo" or self.lexema == "nombre" or self.lexema == "valores" or self.lexema == "evento":
                self.agregar_token(self.lexema, "Identificador", self.linea, self.columna)
                self.estado = 0
                self.i -= 1
            
        #!======================================================
                #?Asignamos nuestras palabras idetinficadores
                #?etiqueta, texto, grupo-radio, grupo-option, boton, EVENTO
            else: 
                self.agregar_token(self.lexema, "Identificador", self.linea, self.columna)  
                self.estado = 0
                self.i -= 1
    
    #!===========================================================
    #? Estados de digitos enteros
    def Estado2(self, caracter :str):
    #!===========================================================    
        '''Estado q2'''
    
        if caracter.isdigit():
            self.lexema +=caracter
            self.columna += 1
            self.estado = 2
               
        elif caracter == ".":
            self.lexema += caracter
            self.columna +=1
            self.estado = 5
        else: 
            self.agregar_token(self.lexema, "Numero: se ingreso un número", self.linea, self.columna)
            self.estado = 0
            self.i -= 1
    
    #!===========================================================
    #? Estado para creación de cadenas
    def Estado3(self, caracter : str):
        if caracter.isalpha() or caracter == "-" or caracter == " ":
            self.lexema += caracter
            self.columna +=1
            self.estado = 3
        elif caracter.isdigit():
            self.lexema +=caracter
            self.columna += 1    
            self.estado = 3
        #elif caracter == "_" or caracter == " ":
        #    self.estado = 1
        #     self.lexema +=caracter
        #     self.columna += 1   
        else: 
            caracter == "'" or caracter == '"'
            self.estado = 7 
            self.lexema +=caracter
            self.columna += 1
            
   
    def Estado7(self, caracter: str):
        if caracter == '"' or caracter == "'":
            self.estado = 7
            self.lexema += caracter
        else:         
            self.agregar_token(self.lexema, "Cadena", self.linea, self.columna)
            self.estado = 0
            self.i -= 1
    #!===========================================================
    #? Estado para creación de simbolos
    def Estado4 (self, caracter : str):
        '''estado q4'''
        if caracter == "[" or caracter == "]" or caracter == "<" or caracter == ">" or caracter == "{" or caracter == "}" or caracter == "," or caracter == ":" or caracter == "#" or caracter == ";": 
            self.lexema += caracter
            self.columna +=1
            self.estado = 4
        
        else:
            self.agregar_token(self.lexema, "Simbolo", self.linea, self.columna)
            self.estado = 0
            self.columna += 1
            self.i -= 1
        
    
    #!===========================================================
    #? Estado para creación de decimales
    def Estado5(self, caracter : str):

        '''Estado q5'''    
        if caracter.isdigit():
            self.lexema +=caracter
            self.columna += 1
            self.estado = 6
        else: 
            pass
    
    #!===========================================================
    #? Estados para creación de decimales
    def Estado6(self, caracter: str):
        '''estado q6'''
        if  caracter.isdigit():
            self.lexema +=caracter
            self.columna += 1
            self.estado = 6            
        else:
            self.agregar_token(self.lexema, "Numero: se ingreso seguido de un decimal", self.linea, self.columna)
            self.estado = 0
            self.i -= 1
    #!===========================================================
    #? Estados para creación de decimales
    
    
    
    def nofunciona(self):
         
        # def estado6(self, caracter):
        #     '''estado q6'''
        #     if caracter == ",":
        #         self.lexema += caracter
        #         self.columna +=1
        
        #     else: 
        #         self.agregar_token(self.lexema, "coma : coma /concatenar/nuevo dato", self.linea, self.columna)
        #         self.estado = 0
        #         self.columna = 1
        #         self.i -=1
        # def estado7(self, caracter):
        #     '''estados q7'''
        #     self.agregar_token(self.lexema, "comillas, simples/dobles", self.linea, self.columna)
        #     self.estado = 0
        #     self.i -=1
        # def estado8(self, caracter):
        #     '''estado q8'''
        #     self.agregar_token(self.lexema, "")
        # def estado9 (self, caracter):
        #     '''estado q9'''
        #     self.agregar_token(self.lexema, "")
        # def estado10(self, caracter):
        #     '''estado q9'''
        #     self.agregar_token(self.lexema, "")
        # def estado11 (self, caracter):
        #     '''estado q9'''
        #     self.agregar_token(self.lexema, "")
                
        #         # self.ListaTokens.append(constructor(lexema, linea, columna,"Sepadadores/ ingreso de opciones"))
                
        #         # elif caracter == ",":
        #         #     self.buffer += caracter
        #         #     columna += 1
        #         #     self.estado = 7
                
        #         # elif caracter == "=":
        #         #     self.buffer += caracter
        #         #     columna += 1
        #         #     self.estado = 8
                
        #         # #! espacios no reconocidos
        #         # elif caracter == "[ \t]":
        #         #     self.buffer += caracter
        #         #     columna += 1
        #         #     self.estado = 13

        #         # elif caracter == "[ \n]":
        #         #     self.buffer += caracter
        #         #     columna += 1
        #         #     self.estado = 14

        #         # elif caracter == "[ \r]":
        #         #     self.buffer += caracter
        #         #     columna += 1
        #         #     self.estado = 15
        #         # #reconoce espacios, ¿funciona? lo averiguaremos
        #         # elif caracter == " ":
        #         #     self.buffer += caracter
        #         #     columna += 1
        #         #     self.estado = 16
        #         # elif caracter == ":":
        #         #     self.buffer += caracter
        #         #     columna += 1
        #         #     self.estado = 17
                
        #         # # elif caracter == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        #         # elif caracter.isdigit(): #! funciona para saber si es numerico
        #         #     self.buffer += caracter
        #         #     columna +=1
        #         #     self.estado = 18

        #         # else: 
        #         #     #! nos dara un error
        #         #     self.ListaErrores.append(Error("Error Caracter desconocido",
        #         #     linea,
                #     columna))
                print("nel")

    def Analizar(self, caracter):
        self.ListaErrores = []
        self.ListaTokens = []
        self.i= 0
        while self.i < len(caracter):
            if self.estado == 0:
                self.Estado0(caracter[self.i])
            elif self.estado == 1:
                self.Estado1(caracter[self.i])
            elif self.estado == 2:
                self.Estado2(caracter[self.i])
            elif self.estado == 3:
                self.Estado3(caracter[self.i])
            elif self.estado == 4:
                self.Estado4(caracter[self.i])
            elif self.estado == 5:
                self.Estado5(caracter[self.i])
            elif self.estado == 6:
                self.Estado6(caracter[self.i])
            elif self.estado == 7:
                self.Estado7(caracter[self.i])
            self.i += 1

    def imprimirTokens(self):
        '''Imprime una tabla con los tokens'''
        x = PrettyTable()
        x.field_names = ["Lexema","linea","columna","tipo"]
        if len(self.ListaTokens) >0:
            for token in self.ListaTokens:
                x.add_row([token.descripcion, token.linea, token.columna,token.tipo])
            print(x)
        else: 
            messagebox.showinfo("Advertencia", "Te falta la información")
        
        self.Tabla_tokens(x.get_html_string(),"tokens")
        return x.get_html_string()

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["Lexema","linea","columna", "tipo"]
        if len(self.ListaErrores) > 0:
            for error_ in self.ListaErrores:
                x.add_row([error_.descripcion, error_.linea, error_.columna, error_.tipo])     
            print(x)
        else: 
            messagebox.showinfo("Advertencia", "Te falta la información")
        
        self.Tabla_tokens(x.get_html_string(),"errores")
        
        return x.get_html_string()


    def iniciar(self):
        self.ListaTokens = []
        self.ListaErrores = [] 
        self.linea = 1
        self.columna= 0
        self.lexema = "" # strings
        self.estado = 1  #
        self.i = 0
    def guardar(self, name: str, cadena: str, abrir: bool = True ):  #? es una libreria por defecto, sirve para manejo de rutas
        ruta = os.path.dirname(os.path.abspath(__file__))+"\\archivos"
        apertura= open("{}\\{}".format(ruta, name), encoding = "utf-8", mode = "w" )
        apertura.write(cadena)
        apertura.close()
        if abrir:
            os.system('start {}\\"{}"'.format(ruta, name))#? format = es para incrustar valores desde codigo a cadena
    def busqueda(self, codigo ):
        self.Analizar(codigo)
        self.Tabla_tokens(codigo)

    def Tabla_tokens(self, cadena, nombre_tab):
        print("su reporte se esta cargando")
        print(" cargando.....")
        print(" cargando ......")
        print("gracias por preferirnos")
        # repo = open("Tabla.html", "w")
        estilo = '''<!DOCTYPE html>
        <html lang="en">
            <head>
                <title>Tabla {1}</title>
                <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
            <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.slim.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"></script>
            </head>
        <body>
        <div class="container">
        <h2>Tabla {1}</h2>  
         <table class="table">
            <thead class="thead-dark">
             {0}
        </table>'''.format(cadena, nombre_tab)  #? 1: nombre_tab, 0: cadena
        self.guardar("{0}.html".format(nombre_tab), estilo, True)#? colocamos falso para abrir después
    

