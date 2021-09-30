from abc import ABC, abstractmethod


class InterfaceComando(ABC):

    @staticmethod
    @abstractmethod
    def execute():
        pass
