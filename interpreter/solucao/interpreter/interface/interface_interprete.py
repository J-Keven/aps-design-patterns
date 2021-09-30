from abc import ABC, abstractmethod


class InterfaceExpression(ABC):

    @staticmethod
    @abstractmethod
    def interpret():
        pass
