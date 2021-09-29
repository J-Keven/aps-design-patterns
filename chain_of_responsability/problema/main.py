"""
    Um exemplo de problema onde há muitas verificações a serem feitas
"""


class Validador(object):
    def validar(self, comida: str):
        if(comida == 'banana'):
            self.__acao1()
        elif(comida == 'carne'):
            self.__acao2()
        elif(comida == 'girasol'):
            self.__acao3()
        elif(comida == 'alface'):
            self.__acao4()
        elif(comida == 'milho'):
            self.__acao5()
        # ...

    def __acao1(self):
        print("O macaco come banana")

    def __acao2(self):
        print("O leão come carne")

    def __acao3(self):
        print("O papagaio come girasol")

    def __acao4(self):
        print("O jabuti come alface")

    def __acao5(self):
        print("A galinha come milho")
    # ...


if __name__ == "__main__":
    v = Validador()
    v.validar('carne')
