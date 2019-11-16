"""
Autor: Daniel Henrique Comério
Resolução do problema _uva10264_ - "The most potent corner"
O que foi necessário: Buscar informações sobre o que são e quais propriedades os cubos N dimensionais possuem, qual a forma 
de calcular a potência, conceitos de lista e manipulação de bits.
Descrição: Inicialmente resgatamos a primeira entrada, ela corresponde ao número de dimensões do cubo. Logo após, sabendo 
que o número de vértices de um cubo de dimensão N é 2^n, calculamos ele, e utilizamos para capturar as 2^n entradas seguintes.
Essas entradas são alocadas em uma lista denominada CUBO contendo N posições, cada uma dessas posições contendo seu respectivo peso.
Em seguida, criamos uma outra lista que é preenchida com as potências referentes a cada um dos vértices. Por fim, tendo em mãos
as potências de cada vértice, é calculado qual é maior soma das potências de dois vértices vizinhos.
"""


while True:
    try:
        dimensao = int(input())
        vertices = 2**dimensao

        cubo = []
        for i in range(vertices):
            peso = int(input())
            cubo.append(peso)


    except EOFError:
        break



    lstPotencias = []
    for i in range(vertices):
        lstPotencias.append(0)

        for j in range(dimensao):
            lstPotencias[i] += cubo[i ^ (1 << j)]


    maiorPotencia = 0   # Maior valor da soma das potências de dois vértices vizinhos
    for i in range(vertices):

        for j in range(dimensao):

            if (lstPotencias[i] + lstPotencias[i ^ (1 << j)]) > maiorPotencia:
                maiorPotencia = lstPotencias[i] + lstPotencias[i ^ (1 << j)]

    print(maiorPotencia)