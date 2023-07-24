#Enunciado
#Elementos individuais de listas
#Muitas vezes, precisamos acessar elementos individuais de listas, o que é possível de ser feito a partir de sua indexação.

#Sabendo disso, crie uma função retornaPenultimoEQuartoElementodeLista() que recebe uma lista e retorne o quarto e o penúltimo elemento desta lista, nesta ordem.

lista = [0, 1, 2, 3, 4, 5, 6]

def retornaPenultimoEQuartoElementodeLista(lista):
    quartoItem = lista[3]
    penultimoItem = lista[-2]
    resultado = quartoItem, penultimoItem

    return resultado
 
retornaPenultimoEQuartoElementodeLista(lista)