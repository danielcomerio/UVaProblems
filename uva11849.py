"""
Autor: Daniel Henrique Comério
Resolução do problema _uva11849_ - "CD"
(Time limit exceeded, porém foram efetuados todos os testes do uDebug referente a esse exercício, os quais todos deram 
os resultados corretos).
O que foi necessário: Conceitos de lista.
Descrição: Inicialmente resgatamos a primeira entrada, ela corresponde à quantidade de CDs possuída tanto pelo primeiro 
quanto pelo segundo amigo. Com base nesses valores de entrada, criamos duas listas, as quais capturam o VALOR (equivalente
a um ID) de cada CD possuído por cada um dos amigos. Posteriormente é comparado os valores da LISTA1 com os da LISTA2, e 
para cada valor contído em ambas as listas, incrementa-se o contador.
"""


while True:

    qntdCD = []
    lista1 = []
    lista2 = []

    try:
        qntdCD = input().strip().split(' ')

        if qntdCD[0] == '0' and qntdCD[1] == '0':
            break

        for i in range(int(qntdCD[0])):
            lista1.append(int(input().strip()))
        
        for j in range(int(qntdCD[1])):
            lista2.append(int(input().strip()))


    except EOFError:
        break


    cont = 0
    for k in range(int(qntdCD[0])):
        
        if lista1[k] in lista2:
            cont += 1

    print(cont)
