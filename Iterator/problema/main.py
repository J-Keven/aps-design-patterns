"""
    Um exemplo de problema simples onde temos uma lista de elementos
    e queremos percorre-la de formas diferentes.
"""

if __name__ == "__main__":
    # lista
    lista = [("a", "b"), ("c", "d"), 3]

    # mostrando na ordem de inserção
    for elemento in lista:
        print(elemento)

    # mostrando na ordem reversa
    for indice in range(len(lista) - 1, -1, -1):
        print(lista[indice])
