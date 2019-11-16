"""
Autor: Daniel Henrique Comério
Resolução do problema _uva10107_ - "What is the Median?"
O que foi necessário: É utilizado conceitos de lista em conjunto da função SORT do python.
Descrição: A cada iteração é adicionado um novo elemento a lista. Logo após, é realizado a ordenação de seus elementos.
Por fim, é refeito o cálculo da nova mediana.
"""


entrada = []

while True:
    try:
        entrada.append(int(input()))

    except EOFError:
        break

    entrada.sort()
    tamanho = len(entrada)
    resto = tamanho%2
    meio = tamanho//2


    if resto != 0:
        print(entrada[meio])

    else:
        print((entrada[meio] + entrada[meio - 1])//2)