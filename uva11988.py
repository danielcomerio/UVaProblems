"""
Autor: Daniel Henrique Comério
Resolução do problema _uva11988_ - "Broken Keyboard (a.k.a. Beiju Text)"
(Time limit exceeded, porém foram efetuados todos os testes do uDebug referente a esse exercício, os quais todos deram 
os resultados corretos).
O que foi necessário: Conceitos de lista.
Descrição: Inicialmente resgatamos a primeira entrada, ela corresponde ao texto a ser verificado, contendo ou não os caracteres
especiais. A cada iteração é verificado qual é o caractere atual, caso ele seja um caractere normal, o adicionamos ao BUFFER,
porém caso ele seja '[' ou ']' todo conteúdo presente no BUFFER é adicionado ou à esquerda ou à direita da SAIDA,dependendo 
apenas do valor da variável booleana CAUDA. Logo após, modificamos os valores das variavéis BUFFER para vazio e da CAUDA para
o valor condizente com o caso executado. A execução termina apenas quando recebe EOF como argumento de entrada.
"""


from collections import deque


while True:

    try:
        entrada = input().strip()

    except EOFError:
        break


    saida = deque()
    buffer = ''
    cauda = True
    i = 0

    while i < len(entrada):

        if entrada[i] == '[':
            
            if cauda:
                saida.append(''.join(buffer))
            else:
                saida.appendleft(''.join(buffer))

            buffer = ''
            cauda = False


        elif entrada[i] == ']':

            if cauda:
                saida.append(''.join(buffer))
            else:
                saida.appendleft(''.join(buffer))

            buffer = ''
            cauda = True

        else:
            buffer += entrada[i]
        
        i += 1
    
    if cauda:
        saida.append(''.join(buffer))
    else:
        saida.appendleft(''.join(buffer))
    
    print((''.join(saida)))