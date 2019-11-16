"""
Autor: Daniel Henrique Comério
Resolução do problema _uva01062_ - "Containers"
O que foi necessário: Conceitos de lista.
Descrição: Inicialmente resgatamos a primeira entrada, ela corresponde à ordem em que os containers irão chegar. Logo após, criamos uma
lista que será responsável por armazenar apenas o último elemento que foi inserido no topo de cada pilha. A cada iteração é verificado se 
o primeiro caractere da entrada é maior que o topo de todas as pilhas (criamos uma nova pilha) ou se ele é igual a algum dos topos 
(não fazemos nada, porque seria como se nós inseríssemos um caractere igual ao outro, o que é desnecessário), e caso as duas alternativas
anteriores falhem, saberemos que algum elemento do topo de alguma das pilhas é maior que tal caractere (analisamos todas as pilhas que 
tenham o topo maior que o primeiro caractere de entrada, mas escolhemos dentre elas, a que tenha o menor caractere, para assim inserirmos
o caractere de entrada).
"""


cont = 1

while True:

    try:
        entrada = input().strip()

    except EOFError:
        break

    if entrada == 'end':
        break

    aux = entrada
    pilhas = []

    for i in range(len(entrada)):

        maior = True
        for i in range(len(pilhas)):
            if pilhas[i] >= aux[0]:
                maior = False
                break


        if maior:
            pilhas.append(aux[0])


        elif pilhas[i] > aux[0]:
            posicao = i

            for j in range(i, len(pilhas)):
                if pilhas[j] > aux[0]:

                    if pilhas[j] < pilhas[posicao]:
                        posicao = j

            pilhas[posicao] = aux[0]

        aux = aux[1:]

    print("Case %d:" % cont, len(pilhas))
    cont += 1