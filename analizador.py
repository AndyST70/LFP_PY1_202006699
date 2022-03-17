from ast import Global
from mysqlx import Column
from pyparsing import col
from error import Error
from Token import constructor
class AnalizadorLexico():
    def __init__(self):
        self.ListaTokens = []
        self.ListaErrores = [] 
        
        # self.i = 0
        #tipo, lexema, linea y columna
        
    # while=?
    def analizador(self, caracter):
        '''Documentación analizador'''
        
        txt_2 = caracter # txt
        #! iniciamos nuestros atributos
        lexema = ""
        estado = 0
        indice = 0 #indice
        #?uso de prueba
        linea = 0
        columna = 0
        for nam in caracter:
            print(nam)
        

            # elif estado == 2:

                        # self.ListaTokens.append(constructor(lexema, linea, columna,"Sepadadores/ ingreso de opciones"))
      

            #     caracter.isalpha(): #! is alpha se utiliza para el manejo de cadenas o bien para reconocer caracteres.
            #     self.buffer += caracter
            #     columna += 1
            #     self.estado = 1

            # elif caracter == "-->":
            #     self.buffer += caracter
            #     columna += 1
            #     self.estado = 2
            
            # elif caracter == "[":
            #     self.buffer += caracter
            #     columna += 1
            #     self.estado = 3
            # elif caracter == "]":
            #     self.buffer += caracter
            #     columna += 1
            #     self.estado = 4

            # elif caracter == '"':
            #     self.buffer += caracter
            #     columna += 1
            #     self.estado = 5
            
            # elif caracter == "'":
            #     self.buffer += caracter
            #     columna += 1
            #     self.estado = 6

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
    
