"""
Adicionar elementos em listas
Quando utilizamos listas, uma das vantagens é que podemos adicionar novos elementos com o passar do tempo. Podemos inserir elementos tanto ao final da lista, como também em uma posição específica.

Sabendo disso, faça uma função adicionarElemento() que recebe uma lista de números e insere o número inteiro 42 no meio da lista (isto é, em sua posição central). Note que a posição de inserção pode variar a depender da quantidade de elementos na lista original.
"""


lista = [30, 40, 50, 60, 70, 80, 90]
    
def adicionarElemento(lista):
    adiciona_valor = 42
    meioDaLista = len(lista) // 2 
    lista.insert(-meioDaLista, adiciona_valor)
    return lista

nova_lista = adicionarElemento(lista)
print(nova_lista)