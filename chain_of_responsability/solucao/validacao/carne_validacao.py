from .interface import InterfaceValidacao


class CarneValidacao(InterfaceValidacao):

    def validar(self, comida: str) -> bool:
        return True if(comida == 'carne') else False

    def acao(self):
        print("O leão come carne")
