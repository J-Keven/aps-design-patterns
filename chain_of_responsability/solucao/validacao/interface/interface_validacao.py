from abc import ABC, abstractmethod


class InterfaceValidacao(ABC):
    """
        Classe abistrata a qual nossas classes de validacões devem seguir
    """

    @abstractmethod
    def validar(self, comida: str) -> bool:
        pass

    @abstractmethod
    def acao(self) -> None:
        pass
