from abc import ABC, abstractclassmethod


class InterfaceIterador(ABC):

    """
        Classe abistrata a qual nossas classes de iteradores devem seguir
    """
    @abstractclassmethod
    def tem_prox(self):
        pass

    @abstractclassmethod
    def prox(self):
        pass
