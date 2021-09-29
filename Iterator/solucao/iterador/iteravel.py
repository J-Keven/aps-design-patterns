from .interface import InterfaceIterador


class Iteravel(InterfaceIterador):
    def __init__(self, colecao, max: int, reverse: bool = False) -> None:
        self._colecao = colecao
        self._indice = (max - 1) if reverse else 0
        self._max = -1 if reverse else max
        self._reverse = reverse

    def prox(self):
        if(self._indice != self._max):
            x = self._colecao[self._indice]
            self._indice += -1 if self._reverse else 1
            return x
        else:
            raise Exception("AtEndOfIteratorException",
                            "O Iterador Chegou ao Fim")

    def tem_prox(self):
        return self._indice != self._max
