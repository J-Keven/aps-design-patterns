from .interface import InterfaceComando


class ComandoLigarLuz(InterfaceComando):
    def __init__(self, luz):
        self._luz = luz

    def execute(self):
        self._luz.ligarLuz()


class ComandoDesligarLuz(InterfaceComando):
    def __init__(self, luz):
        self._luz = luz

    def execute(self):
        self._luz.desligarLuz()
