
from interpreter import Numero, Add, Sub, InterfaceInterprete


if __name__ == "__main__":
    sequencia = "5 + 4 - 3 + 7 - 2"
    print(sequencia)

    tokens = sequencia.split(" ")
    print(tokens)

    """
        imagine aqui um método de processamento que
        converte a string nas expressões matemáticas
    """
    listaAbistrata: list[InterfaceInterprete] = []
    listaAbistrata.append(Add(Numero(tokens[0]), Numero(tokens[2])))    # 5 + 4
    listaAbistrata.append(
        Sub(listaAbistrata[0],
            Numero(tokens[4])))               # ^ - 3
    listaAbistrata.append(
        Add(listaAbistrata[1],
            Numero(tokens[6])))               # ^ + 7
    listaAbistrata.append(
        Sub(listaAbistrata[2],
            Numero(tokens[8])))               # ^ - 2

    listA = listaAbistrata.pop()

    # Representação da árvore
    print(listA)

    # Resultado do cálculo
    print(listA.interpret())
