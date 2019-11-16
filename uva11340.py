"""
Autor: Daniel Henrique Comério
Resolução do problema _uva11340_ - "Newspaper"
(Time limit exceeded, porém foram efetuados todos os testes do uDebug referente a esse exercício, os quais todos deram 
os resultados corretos).
O que foi necessário: Conceitos de dicionário.
Descrição: Inicialmente resgatamos as entradas referentes aos caracteres que possuem custo. Logo após, criamos um dicionário,
para receber essas informações, mais especificamente ele recebe como chave o CARACTERE e como valor o CUSTO. Para cada caractere
do texto de entrada, é verificado se esse está dentro do dicionário, ou seja, se possue algum custo. A soma do custo de cada 
caractere do texto de entrada resulta no custo final do artigo.
"""


while True:

    try:
        artigos = input()
        for i in range(int(artigos)):
            dic = {}
            lst = []

            caracteres = input()
            for j in range(int(caracteres)):
                lst = input().split(' ')
                dic[lst[0]] = int(lst[1])
        
            valor = 0.0
            linhas = input()
            for k in range(int(linhas)):

                linha = input()
                for l in range(len(linha)):
                    if linha[l] in dic:
                        valor += dic[linha[l]]

            valor = valor/100
            print("%.2f" % valor + '$')

        break

    except EOFError:
        break