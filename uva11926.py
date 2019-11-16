"""
Autor: Daniel Henrique Comério
Resolução do problema _uva11926_ - "Multitasking"
(Time limit exceeded, porém foram efetuados todos os testes do uDebug referente a esse exercício, os quais todos deram 
os resultados corretos).
O que foi necessário: Conceitos de lista.
Descrição: Inicialmente resgatamos a primeira entrada referente ao primeiro caso, ela corresponde tanto à quantidade
de tarefas únicas quanto à de tarefas repetitivas. Logo após, criamos duas listas de listas, sendo uma responsável por 
armazenar os valores das tarefas únicas e a outra por armazenar os valores das tarefas repetitivas. A cada entrada de uma 
nova tarefa, é verificado se a mesma está em conflito com alguma anterior, caso esteja, imediatamente é retornado o valor
de "CONFLICT", porém o preocessamento continua até terminar as tarefas restantes para que seja possível chegar na linha do 
próximo caso a ser verificado, e caso não esteja em conflito, o processamento continua normalmente até acabar, e quando
acaba, retorna o valor de "NO CONFLICT".
"""

from copy import deepcopy


def verificaConflito(tarefaLista, tarefaInput):
    conflito = False

    if (tarefaInput[0] > tarefaLista[0] and tarefaInput[0] < tarefaLista[1]) or (tarefaInput[1] > tarefaLista[0] and tarefaInput[1] < tarefaLista[1]):
        conflito = True

    elif (tarefaInput[0] <= tarefaLista[0]) and (tarefaInput[1] >= tarefaLista[1]):
        conflito = True
    
    return conflito


def verificaConflitoSimples(listaTarefas, tarefa):
    conflito = False

    for i in range(len(listaTarefas)):
        conflito = verificaConflito(listaTarefas[i], tarefa)

        if conflito:
            break

    return conflito


def verificaConflitoRepetitivoSimples(listaTarefas, tarefa):
    conflito = False

    for i in range(len(listaTarefas)):
        tarefa2 = deepcopy(tarefa)

        while tarefa2[0] <= 1000000:
            conflito = verificaConflito(listaTarefas[i], tarefa2)

            if conflito:
                break

            tarefa2[0] += tarefa2[2]
            tarefa2[1] += tarefa2[2]


        if conflito:
            break

    return conflito


def verificaConflitoRepetitivo(listaTarefas, tarefa):
    conflito = False
    listaTarefas2 = deepcopy(listaTarefas)

    for i in range(len(listaTarefas2)):

        while listaTarefas2[i][0] <= 1000000:
            tarefa2 = deepcopy(tarefa)

            while tarefa2[0] <= 1000000:
                conflito = verificaConflito(listaTarefas2[i], tarefa2)

                if conflito:
                    break

                tarefa2[0] += tarefa2[2]
                tarefa2[1] += tarefa2[2]


            if conflito:
                break

            listaTarefas2[i][0] += listaTarefas2[i][2]
            listaTarefas2[i][1] += listaTarefas2[i][2]

        if conflito:
            break

    return conflito




while True:

    qntdTarefas = []
    lista1 = []
    lista2 = []
    linha = ''
    conflito = False

    try:
        qntdTarefas = input().strip().split(' ')

        if qntdTarefas[0] == '0' and qntdTarefas[1] == '0':
            break

        for i in range(int(qntdTarefas[0])):
            linha = input().strip().split(' ')

            if not conflito:
                linha[0] = int(linha[0])
                linha[1] = int(linha[1])

                conflito = verificaConflitoSimples(lista1, linha)

                lista1.append(linha)


        for j in range(int(qntdTarefas[1])):
            linha = input().strip().split(' ')

            if not conflito:
                linha[0] = int(linha[0])
                linha[1] = int(linha[1])
                linha[2] = int(linha[2])
                
                conflito = verificaConflitoRepetitivoSimples(lista1, linha)

                if not conflito:
                    conflito = verificaConflitoRepetitivo(lista2, linha)

                lista2.append(linha)

    except EOFError:
        break


    if conflito:
        print("CONFLICT")
    else:
        print("NO CONFLICT")