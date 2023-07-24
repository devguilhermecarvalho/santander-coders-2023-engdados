"""
Indexação de listas e último elemento
Uma lista possui n elementos, sendo comum executarmos determinadas ações em um elemento de determinada posição. Por exemplo, podemos substituir o elemento da primeira posição da lista por outro valor desejado. Quando selecionamos um elemento, chamamos isto de indexação.

Sendo assim, escreva uma função ultimoElemento() em python que recebe uma lista e retorna o último elemento da lista.
"""
def ultimoElemento(lista):
    if not lista:
        return None
    return lista[-1]


minha_lista = [1, 2, 3, 4, 5]
ultimo_elemento = ultimoElemento(minha_lista)
print("Último elemento:", ultimo_elemento)