"""
Remover elementos de listas
Considere que uma empresa desenvolveu uma aplicação que solicita ao usuáriouma dada informação, como, por exemplo, o segundo nome deste usuário. O programa recebe essa informação e armazena em uma lista de strings. Entretanto, caso um usuário acidentalmente não tenha preenchido esta informação, a lista conterá elementos vazios. Por exemplo, dada uma lista com 5 nomes: listaDeNomes = ['Araújo', 'Alexandre', 'Silva', 'Flávio', ''], note que o último elemento da lista é apenas uma string vazia representada pelas aspas vazias.

Sabendo disso, faça uma função removerElementosVazios() que recebe uma lista de nomes e retorna a lista sem os elementos vazios.
# """

listaDeNomes = ['Araújo', 'Alexandre', '', 'Silva', 'Flávio', '']

def removerElementosVazios(listaDeNomes):
    nomes_sem_vazios = [nome for nome in listaDeNomes if nome != '']
    return nomes_sem_vazios

listaSemVazios = removerElementosVazios(listaDeNomes)
resultado = list(listaSemVazios)

print(resultado)

