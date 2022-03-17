
from error import Error
from Token import constructor
class AnalizadorLexico():
    def __init__(self):
        self.ListaTokens = []
        self.ListaErrores = [] 
        self.linea = 1
        self.columna= 1
        self.lexema = ""
        self.estado = 0
        self.i =0
        #tipo, lexema, linea y columna
    # while=?
    def agregar_token(self, caracter, token, linea, columna ):
        self.ListaTokens.append(constructor(caracter, linea, columna, token))
        self.lexema = ""
    def error_append(self, caracter, linea, columna,  token):
        self.ListaErrores.append(Error("caracter: ", caracter, "linea: ", linea, "columna: ", columna))

    def Estado0(self, caracter):
        '''Documentación analizador'''                   
            # elif estado == 2: 
        if caracter.isalpha():#! is alpha se utiliza para el manejo de cadenas o bien para reconocer caracteres.
            self.lexema += caracter
            self.columna +=1
            self.estado = 1

        elif caracter == "->>":
            self.lexema += caracter
            self.columna += 1
            self.estado = 2

        elif caracter =="[" or caracter == "]":
            self.lexema += caracter
            self.columna += 1
            self.estado = 3

        elif caracter == "<" or caracter == ">":
            self.lexema += caracter
            self.columna += 1
            self.estado = 4

        elif caracter =="{" or caracter == "}":
            self.lexema += caracter
            self.columna += 1
            self.estado = 5

        elif caracter ==",":
            self.lexema += caracter
            self.columna += 1
            self.estado = 6
        
        elif caracter =="'" or caracter == '"':
            self.lexema += caracter
            self.columna +=1
            self.estado = 7
        
        elif caracter ==":":
            self.lexema += caracter
            self.columna +=1
            self.estado = 8

        elif caracter.isdigit():
            self.lexema += caracter
            self.columna +=1
            self.estado = 9
        
        elif caracter == "&":
            self.lexema += caracter
            self.columna += 1
            self.estado =10
        
        elif caracter == "\n":
            self.linea += 1
            self.columna = 1 
        
        elif caracter in ["\t", " "]:
            self.columna +=1
        
        elif caracter == "$":
            pass

        elif caracter == "\r":
            pass

        else:
            self.lexema += caracter
              #! nos dara un error
            self.ListaErrores.append(Error("Error Caracter desconocido",
            self.linea,
            self.columna)) 
    def estado1(self, caracter):
        if caracter.alpha():
            self.lexema += caracter
            self.columna +=1
        else:
         #!===================================================
                #? Asignamos nuestras palabras reservadas
                #? formulario, tipo, valor, fondo, nombre
                #? valores, evento

            if self.lexema == "formulario" or self.lexema == "tipo" or self.lexema == "valor" or self.lexema == "fondo" or self.lexema == "nombre" or  self.lexema == "valores" or self.lexema == "evento" :
                self.agregar_token(self.lexema, "palabra reservada, seguida de letras minusculas", self.linea, self.columna) 
            self.estado = 0
            self.columna += 1
            self.i -= 1
    #!===========================================================0
    #? Estados de simbolos
    def estado2(self, caracter):
        if caracter == "->>":
            self.lexema += caracter
            self.columna +=1
        else:
            self.agregar_token (self.lexema, "->> : Ingreso", self.linea, self.columna)
            self.estado = 0
            self.columna = 1
            self.i -=1
    def estado3(self, caracter):
        if caracter == "[" or caracter == "]":
            self.lexema += caracter
            self.columna +=1
     

            

            
            # self.ListaTokens.append(constructor(lexema, linea, columna,"Sepadadores/ ingreso de opciones"))
            
            # elif caracter == ",":
            #     self.buffer += caracter
            #     columna += 1
            #     self.estado = 7
            
            # elif caracter == "=":
            #     self.buffer += caracter
            #     columna += 1
            #     self.estado = 8
            
            # #! espacios no reconocidos
            # elif caracter == "[ \t]":
            #     self.buffer += caracter
            #     columna += 1
            #     self.estado = 13

            # elif caracter == "[ \n]":
            #     self.buffer += caracter
            #     columna += 1
            #     self.estado = 14

            # elif caracter == "[ \r]":
            #     self.buffer += caracter
            #     columna += 1
            #     self.estado = 15
            # #reconoce espacios, ¿funciona? lo averiguaremos
            # elif caracter == " ":
            #     self.buffer += caracter
            #     columna += 1
            #     self.estado = 16
            # elif caracter == ":":
            #     self.buffer += caracter
            #     columna += 1
            #     self.estado = 17
            
            # # elif caracter == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            # elif caracter.isdigit(): #! funciona para saber si es numerico
            #     self.buffer += caracter
            #     columna +=1
            #     self.estado = 18

            # else: 
            #     #! nos dara un error
            #     self.ListaErrores.append(Error("Error Caracter desconocido",
            #     linea,
            #     columna))

    def Imprimir_Tokens(self):
        print("Lista tokens")
        for a in self.ListaTokens:
            a.Imprimir_Tokens()
    
