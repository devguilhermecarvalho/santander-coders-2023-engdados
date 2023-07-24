""" Subtraindo elementos usando funções de alta ordem

Em programação, temos que pensar não apenas na implementação do código propriamente dita para execução correta da tarefa desejada, como também na melhor forma de realizar esta implementação. Com isso, paradigmas de programação foram criados para auxiliar o programador a pensar diferente.

Um desses paradigmas é o uso de funções de alta ordem, o que permite que realizemos diversas operações em coleções (listas, tuplas, arrays, etc) sem o uso de loops explicitamente.

Um dos usos mais comuns é o uso de funções reduce, responsáveis por acumular uma operação ao longo de uma coleção. Sabendo disso, implemente uma função reduceSub() que recebe uma lista, e então faz uso do reduce para realizar a subtração dos números da lista com base no valor inicial 3.
"""

from functools import reduce

lista = list(range(1, 31))

def subtrair(a, b):
    return a - b

def reduceSub(lista):
    valor_inicial = 3
    resultadoReduce = reduce(subtrair, lista, valor_inicial)
    return resultadoReduce

resultado = reduceSub(lista)

print(resultado)