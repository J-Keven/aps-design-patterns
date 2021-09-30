from .interface import InterfaceExpression


class Numero(InterfaceExpression):

    def __init__(self, value):
        self._value = int(value)

    def interpret(self):
        return self._value

    def __repr__(self):
        return str(self._value)


class Add(InterfaceExpression):

    def __init__(self, esquerda, direita):
        self._esquerda = esquerda
        self._direita = direita

    def interpret(self):
        return self._esquerda.interpret() + self._direita.interpret()

    def __repr__(self):
        return f"({self._esquerda} Add {self._direita})"


class Sub(InterfaceExpression):

    def __init__(self, esquerda, direita):
        self._esquerda = esquerda
        self._direita = direita

    def interpret(self):
        return self._esquerda.interpret() - self._direita.interpret()

    def __repr__(self):
        return f"({self._esquerda} Sub {self._direita})"
