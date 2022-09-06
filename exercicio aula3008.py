from functools import reduce


lista = [100, 248.90, 88, 124.90]

def desconto (preco):
    return preco * (1-0.1)

lista_desconto = map(lambda x: desconto(x), lista)
print(list(lista_desconto))

valor_maior = filter(lambda x: x>100, lista)
print(list(valor_maior))

lista_soma = reduce(lambda x, y:x + y, lista, 0)
print(lista_soma)