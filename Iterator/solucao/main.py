from iterador import Iteravel

if __name__ == "__main__":
    # lista
    lista = [("a", "b"), ("c", "d"), 3]

    # mostrando na ordem de inserção
    i = Iteravel(lista, 3)
    while i.tem_prox():
        print(i.prox())

    # mostrando na ordem reversa
    ir = Iteravel(lista, 3, reverse=True)
    while ir.tem_prox():
        print(ir.prox())
