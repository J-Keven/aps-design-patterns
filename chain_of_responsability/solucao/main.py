from validacao import BananaValidacao, CarneValidacao


class Validador(object):

    def __init__(self) -> None:
        self._validacoes = [
            BananaValidacao(),
            CarneValidacao(),
        ]

    def validacao(self, comida: str):
        for v in self._validacoes:
            if(v.validar(comida)):
                return v.acao()


if __name__ == "__main__":
    v = Validador()
    v.validacao('carne')
