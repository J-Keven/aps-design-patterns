from abc import ABC, abstractmethod


class InterfaceIterador(ABC):

    """
        Classe abistrata a qual nossas classes de iteradores devem seguir
    """
    @abstractmethod
    def tem_prox(self):
        pass

    @abstractmethod
    def prox(self):
        pass
