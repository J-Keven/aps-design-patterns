from abc import ABC, abstractclassmethod


class InterfaceValidacao(ABC):
    """
        Classe abistrata a qual nossas classes de validacões devem seguir
    """

    @abstractclassmethod
    def validar(self, comida: str) -> bool:
        pass

    @abstractclassmethod
    def acao(self) -> None:
        pass
