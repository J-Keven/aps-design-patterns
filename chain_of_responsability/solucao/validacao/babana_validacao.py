from .interface import InterfaceValidacao


class BananaValidacao(InterfaceValidacao):

    def validar(self, comida: str) -> bool:
        return True if(comida == 'banana') else False

    def acao(self):
        print("O macaco come banana")
