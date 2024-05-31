def distancia_hamming(a, b):
    """
    Recebe duas strings de mesmo tamanho, a e b.
    Devolve a distância de Hamming entre as duas.
    """
    distancia_hamming = 0 
    for i in range(len(a)):
        for j in a[i]:
            if j != b[i]:
                distancia_hamming += 1
                
    return distancia_hamming

def minima_distancia(alvo, candidatos):
    """
    Recebe uma string alvo e uma lista de strings candidatas.
    Devolve um par contendo a string candidata com menor distância
    de Hamming até o alvo, além da distância.

    Exemplo de uso: sequencia, valor = minima_distancia(alvo, candidatos)
    """

    menor_distancia = distancia_hamming(alvo,candidatos[0])
    menor_distancia_candidato = candidatos[0]
    for candidato in candidatos:
        if distancia_hamming(alvo,candidato) < menor_distancia:
            menor_distancia = distancia_hamming(alvo,candidato)
            menor_distancia_candidato = candidato

    return menor_distancia_candidato, menor_distancia

def janela(sequencia, indice_inicial, tamanho_janela):
    """
    Recebe uma string, um índice inicial e o tamanho da janela.
    Devolve uma string correspondente à janela da sequência começando
    no índice inicial fornecido.

    Exemplo: janela('ABCDEFGHIJ', 2, 3) devolve 'CDE'.
    """
    janela = []
    for posicao in range(indice_inicial,indice_inicial+tamanho_janela):
        janela.append(sequencia[posicao])
    janela = "".join(janela)
    return janela

def distancia_janela(a, b, indice_inicial, tamanho_janela):
    """
    Recebe duas strings a e b, um índice inicial e o tamanho da janela.
    Devolve a distância de Hamming entre as respectivas janelas
    das strings a e b.

    Exemplo: distancia_janela('AAABBB', 'AABABB', 1, 4) devolve 2,
    que é a distância entre 'AABB' e 'ABAB'
    """
    janela_1 = janela(a, indice_inicial, tamanho_janela)
    janela_2 = janela(b, indice_inicial, tamanho_janela)
    distancia_1_2 = distancia_hamming(janela_1, janela_2)
    return distancia_1_2


def diferencas(a, b, tamanho_janela):
    """
    Recebe duas sequências (strings) a e b e o tamanho da janela.
    Devolve uma lista com todas as posições em que as janelas de a e de b
    apresentam diferença SIGNIFICATIVa, isto é, de pelo menos 1/3 do tamanho
    da janela.
    """

    diferencas = []

    i = 0
    janelas_a = []
    janelas_b = []
    posicoes_i = []
    while i != len(a):
        janelas_a.append(janela(a, i, tamanho_janela))
        janelas_b.append(janela(b, i, tamanho_janela))
        posicoes_i.append(i)
        i += tamanho_janela

    for i in range(len(posicoes_i)):
        diferenca_a_b = distancia_hamming(janelas_a[i], janelas_b[i])
        if diferenca_a_b >= tamanho_janela/3:
            diferencas.append(posicoes_i[i])

    return diferencas


