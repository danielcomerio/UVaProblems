"""
Autor: Daniel Henrique Comério
Resolução do problema _uva12405_ - "Scarecrow"
O que foi necessário: Conceitos de lista e da lógica de proteção do espantalho com base nas posições anteriores.
Descrição: Inicialmente resgatamos a primeira entrada, ela corresponde ao número de casos a serem processados. Logo após, recebemos a
entrada que corresponde à plantação que é armazenada em uma string de tamanho N, a qual posteriormente transformamos em uma lista de
N posições. A cada iteração, verificamos se o caractere atual é um '.', caso seja, verificamos se este ponto está sendo protegido por
algum espantalho, se ele não estiver, incrementamos o número de espantalhos. Sempre ao final de cada iteração, verificamos a posição
do último espantalho na plantação e caso ele esteja a menos de duas posições, da posiçã atual (sempre que iteramos, excluímos o
primeiro elemento da lista e baseamos nosso processamento sempre na primeira posição até a lista estar vazia), significa que a próxima
posição estará protegida, caso contrário, estará desprotegida.
"""


cases = int(input().strip())

for i in range(cases):
    scarescrow = 0
    lastScarecrow = -2
    protected = False

    input()
    field = input().strip()
    field = [field[z:z+1] for z in range(len(field))]

    while len(field) > 0:

        if field[0] == '.':
            if protected:
                lastScarecrow -= 1
            else:
                lastScarecrow = 0
                scarescrow += 1
        else:
            lastScarecrow -= 1

        if lastScarecrow > -2:
            protected = True
        else:
            protected = False

        field = field[1:]

    print("Case " + str(i + 1) + ": " + str(scarescrow))