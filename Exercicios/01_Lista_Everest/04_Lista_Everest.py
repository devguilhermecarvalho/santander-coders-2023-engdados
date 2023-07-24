"""
Ordenando listas
Em um sistema, comumente utilizamos listas para armazenamento de dados. Entretanto, existem casos em que torna-se necessário criarmos um padrão de organização dos dados. Por exemplo, podemos organizar um cadastro de clientes pela idade destes usuários. Este procedimento de organização é conhecido como ordenação.

Sabendo disso, crie uma função chamada ordena_lista() que recebe uma lista de elementos e ordene-os em ordem decrescente. A função possui como parâmetro a lista a ser ordenada e retorna a mesma lista ordenada de forma decrescente.
"""

lista = [48, 34, 25, 72, 80, 18, 39, 50]

def ordena_lista(lista):
    lista_ordenada = sorted(lista, reverse=True)
    
    return lista_ordenada

resultado = ordena_lista(lista)
print(resultado)