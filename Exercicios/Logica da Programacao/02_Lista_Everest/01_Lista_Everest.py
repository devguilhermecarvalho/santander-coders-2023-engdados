""" Encontrando números divisíveis por 7
Uma forma "pythonica" de iterarmos por listas é por meio de compreensão de listas, que substitui o uso de um laço de repetição for tal como implementamos tradicionalmente para a criação de novas listas.

Sabendo disso, digamos que em um sistema desejemos buscar, entre 1000 usuários, apenas aqueles cujo ID é divisível por 7. Faça uma função numerosDiv7() para este sistema que receba uma lista A de 1000 elementos e retorne uma lista apenas com os elementos de A que são divisíveis por 7.

OBS: Caso existam elementos repetidos na lista, a saída deverá exibir apenas os elementos únicos divisíveis por 7. E se não houver elementos divisíveis por 7, o programa deve retornar uma lista vazia. """

listaA = list(range(1, 1001))

def numerosDiv7(listaA):
    div7 = [num for num in listaA if num % 7 == 0]
    numeros_unicos = list(set(div7))
    return numeros_unicos

resultado = numerosDiv7(listaA)

if resultado:
    print(resultado)
else:
    print("Não números divisíveis por 7 na lista.")
