class Error: 
    def __init__(self, descripcion: str, linea, columna):

        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna
    def imprimir_error(self):
        print(self.descripcion, self.linea, self.columna)
        