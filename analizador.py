from error import Error
from token_ import Lexema

class AnalizadorLexico:
    def __init__(self) -> None:
        pass
        self.ListaTokens = []
        self.ListaErrores = []
        self.Linea = 1
        self.columna = 0
        self.buffer = ""
        self.estado = 0
        self.i = 0

