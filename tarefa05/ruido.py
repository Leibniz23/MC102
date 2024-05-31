import sequencias

def receber_candidatas():
    """
    Pede uma lista de sequências candidatas ao usuário e devolve essa lista
    """

    n = int(input())
    candidatas = []
    for sequencia in range(n):
        sequencia = input()
        candidatas.append(sequencia)

    return candidatas

def main():
    alvo = input()
    candidatas = receber_candidatas()
    menor_distancia = sequencias.minima_distancia(alvo, candidatas)
    for sequencia in candidatas:
        distancia = sequencias.distancia_hamming(sequencia, alvo)
        if distancia < menor_distancia[1]:
            menor_distancia[1] = distancia
            menor_distancia[0] = sequencia

    print("Sequência mais próxima: ", menor_distancia[0])
    print("Distância de Hamming: ", menor_distancia[1])
    
main()
