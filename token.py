class constructor: 
    '''Clase token'''
    def __init__(self, descripcion : str, linea, columna : int, tipo) -> None:

        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna
        self.tipo = tipo
    def imprimir_data(self):
        print(self.descripcion, self.linea, self.columna, self.tipo)
        