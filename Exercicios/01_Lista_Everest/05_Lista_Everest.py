"""
Elemento e índice
Em python, muitas vezes é útil iterarmos tanto pelos elementos quanto pelos índices de listas. Sabendo disso, crie uma função calculaPotencia() que recebe uma lista A e retorna uma lista B, tal que os elementos desta lista sejam iguais aos elementos da lista A elevado a potência igual ao índice do respectivo elemento.

Por exemplo, dado uma lista A = [2,5,6], gere uma lista B = [2^0, 5^1, 6^2].
"""

listaA = [2, 5, 6]

def calculaPotencia(listaA):
    listaB = [num ** indice for indice, num in enumerate(listaA)]
    return listaB

listaB = calculaPotencia(listaA)
print(listaB)
	