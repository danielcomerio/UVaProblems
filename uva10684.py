"""
Autor: Daniel Henrique Comério
Resolução do problema _uva10684_ - "The jackpot"
O que foi necessário: Conceitos de lista e da lógica de incrementação correta de uma variável responsável por achar o custo máximo do problema.
Descrição: Inicialmente resgatamos a primeira entrada, ela corresponde à quantidade de custos que virão a seguir. Logo após, recebemos como
parâmetro de entrada as Y linhas contendo os N custos. Para cada custo de entrada, o incrementamos a uma variável denominada também de CUSTO,
caso essa incrementação dê um CUSTO final positivo, o processamento continua normalmente, caso contrário, se o CUSTO for menor que 0, resetamos
o CUSTO para 0 e voltamos a fazer o processamento. Sempre que o CUSTO é incrementado, é verificado se ele é maior que a variável CUSTO-MAXIMO,
caso seja, fazemos o CUSTO-MAXIMO receber o valor de CUSTO, pois é o maior valor verificado até então.
"""


while True:
    qntdEntrada = input().strip()
    while qntdEntrada == '':
        qntdEntrada = input().strip()
    qntdEntrada = int(qntdEntrada)

    custoMaximo = 0
    custo = 0
    cont = 0

    if qntdEntrada != '':
        qntdEntrada = int(qntdEntrada)

        while cont < qntdEntrada:
            entrada = input().strip().split()
            while entrada == '':
                entrada = input().strip().split()

            cont += len(entrada)

            for j in range(len(entrada)):
                if (int(custo) + int(entrada[j])) >= 0:
                    custo += int(entrada[j])

                    if custo > custoMaximo:
                        custoMaximo = custo

                else:
                    custo = 0


    if qntdEntrada == 0:
        break

    if custoMaximo > 0:
        print("The maximum winning streak is " + str(custoMaximo) + ".")

    else:
        print("Losing streak.")