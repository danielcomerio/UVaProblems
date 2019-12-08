"""
Autor: Daniel Henrique Comério
Resolução do problema _uva280_ - "Vertex"
(Time limit exceeded, porém foram efetuados todos os testes do uDebug referente a esse exercício, os quais todos deram os resultados corretos).
O que foi necessário: Conceitos de lista (inclusive importamos a biblioteca DEQUE do python para fazer manipulações mais eficientes) e de busca
em profundidade em grafos.
Descrição: Inicialmente resgatamos a primeira entrada, ela corresponde à quantidade de vértices do grafo a seguir. Logo após, criamos o grafo que
será tradado como uma lista de listas que será responsável por armazenar as arestas de cada vértice. A próxima entrada corresponde aos vértices que
serão tratados como vértices iniciais da pesquisa em profundidade, para verificar quais vértices não serão acessíveis a partir de cada um deles.
A função de pesquisa em profundidade retorna todos os vértices acessíveis pelo vértice inicial. Posteriormente, com base nos vértices acessíveis
e dos vértices existentes, achamos os vértices inacessíveis com a subtação dos existentes pelos acessíveis. Continuamos com o processamento até
que os vértices a serem verificados do grafo atual acabem e que não existam mais grafos para processar.
"""


from collections import deque

def pesqProfundidade(grafo, vertice):
  visitados = set() 
  arestas = deque([vertice - 1])
  
  while len(arestas) > 0:
    v = arestas.pop()
    for e in grafo[int(v)]:
        e = str(int(e) - 1)
        if not e in visitados:
            visitados.add(e)
            arestas.append(e)
  
  return visitados


qntdVertices = int(input().strip())

while qntdVertices > 0:

    grafo = []
    for x in range(qntdVertices):
        grafo.append([])

    vertices = input().strip().split(' ')

    while vertices != ['0']:
        grafo[ int(vertices[0]) - 1 ] += vertices[1:-1]
        vertices = input().strip().split(' ')

    raizes = input().strip().split(' ')

    for vertice in range(1, int(raizes[0]) + 1):
        nVisitados = []
        for y in range(qntdVertices):
            nVisitados.append(str(y + 1))

        visitados = pesqProfundidade(grafo, int(raizes[vertice]))

        for k in visitados:
            if str(int(k) + 1) in nVisitados:
                nVisitados.remove(str(int(k) + 1))

        saida = ''
        saida += str(len(nVisitados))
        for z in nVisitados:
            saida += ' ' + z
        
        print(saida)
   
   
    qntdVertices = int(input().strip())