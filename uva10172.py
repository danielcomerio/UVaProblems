"""
Autor: Daniel Henrique Comério
Resolução do problema _uva10172_ - "The Lonesome Cargo Distributor"
O que foi necessário: Conceitos de lista, pilha e fila. Além disso, foi necessário extrema atenção na leitura do enunciado,
devido ao seu tamanho extenso e da sua leitura um tanto complicada e ambígua.
Descrição: Inicialmente resgatamos a primeira entrada, ela corresponde ao número de casos que serão analisados. Logo após, vem as informações
de um caso específico, seguido de N linhas de informação. É criado então uma lista contendo N filas, e logo após criamosuma pilha que corresponde
ao manipulador de cargas, sendo responsável por fazer a carga e a descarga das filas. De acordo com as condições impostas, o manipulador de cargas 
verifica se o topo de sua pilha condiz com a estação que atualmente está visitando, caso seja verdadeiro, ele descarrega (mais especificamente exclui
da pilha, como se tivesse sido entregue ao seu devido lugar), caso seja falso, a pilha incrementaa a fila da estação, e se nenhuma das anteriores forem
verdadeiras, ele passa para a próxima etapa. Nela, adicionamos à pilha as cargas da fila da estação atual até que a pilha fique cheia ou a fila fique 
vazia, o que ocorrer primeiro. Logo após, o carregador passa para a próxima estação, e o processo se repete até que todas as cargas tenham sido
devidamente descarregadas. Ao longo de todo o processo é somado o tempo gasto em cada uma das etapas, até que cheguemos no tempo total utilizado para
a conclusão das descargas.
"""


casos = int(input())

for z in range(casos):
    caso = input().split()

    numEstacoes = int(caso[0])
    capCarregador = int(caso[1])
    capPlatB = int(caso[2])

    tempo = 0
    cargas = 0
    pilha = []
    filas = []

    for i in range(numEstacoes):
        estacao = input().split()
        cargas += int(estacao[0])
        filas.append(estacao[1:])

    while True:
        for i in range(1, len(filas) + 1):
            while pilha != []:
                # Coloca o topo da pilha na Plataforma A da estação atual
                if pilha[len(pilha)-1] == str(i):
                    pilha = pilha[:-1]
                    cargas -= 1
                # Fila dá append no topo da pilha
                elif len(filas[(i-1)]) < capPlatB:
                    filas[(i-1)].append(pilha[len(pilha)-1])
                    pilha = pilha[:-1]
                # O topo da pilha não corresponde àquela estação e a plataforma B está com sua fila cheia
                else:
                    break
                tempo += 1

            # Preenche a pilha até ficar cheia ou a fila da plataforma B ficar vazia, o que ocorrer primeiro        
            while filas[(i-1)] != [] and len(pilha) < capCarregador:
                pilha.append(filas[(i-1)][0])
                filas[(i-1)] = filas[(i-1)][1:]
                tempo += 1
            # Assim que todas as cargas forem entregues a seus devidos lugares, o caso termina
            if cargas == 0:
                break
            tempo += 2

        if cargas == 0:
            break

    print(tempo)