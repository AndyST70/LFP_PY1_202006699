class Error: 
    def __init__(self, descripcion:str, tipo, linea, columna):

        self.descripcion = descripcion
        self.linea = linea
        self.tipo = tipo
        self.columna = columna
    def imprimir_error(self):
        print(self.descripcion, self.tipo, self.linea, self.columna)
        
