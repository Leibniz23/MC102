import math

def ler_entradas():
    """
    Coleta as entradas do teclado e devolve uma lista de inteiros
    """
    entradas = input().split()
    entradas = list(map(int, entradas))
    return entradas

def calcular_thd(lista, index, onda, k=1):
    """
    Calcula o THD de uma lista a partir do elemento k (por padrão é o segundo elemento da lista)
    com base na onda fundamental dada até o index indicado, e retorna o valor do THD em porcentagem
    """
    soma = 0
    for i in range(k,index+1):
        soma += lista[i]**2
    thd = (math.sqrt(soma)/onda)*100
    return thd

def saidas(n_harmonicos, thd_crit, thd_geral):
    """
    Mostra na tela as saídas pedidas
    """
    print(f"Número de harmônicos críticos: {n_harmonicos}")
    print(f"THD de harmônicos críticos: {thd_crit:.2f} %")
    print(f"THD de todos os harmônicos: {thd_geral:.2f} %")

def janela(ind_i, ind_f, lista):
    """
    Cria uma nova lista com base na lista dada, começando no índice ind_i e terminando em ind_f (inclusivo)
    """
    return lista[ind_i:ind_f+1]

def gerar_grupos(lista):
    """
    Cria um dicionário contendo todas as combinações de 3 grupos distintos possíveis
    """
    grupos = {}
    n = 0
    for i in range(len(lista)-2):
        for k in range(i+1, len(lista)-1):
            grupos[n] = [janela(0, i, lista), janela(i+1, k, lista), janela(k+1, len(lista), lista)]
            n += 1
    return grupos

def encontrar_maiores(grupos):
    """
    Encontra, em cada conjunto de grupo possível, o maior THD desse conjunto e retorna esse valor
    junto com sua chave no dicionário
    """
    maiores = {}
    for n in range(len(grupos)):
        thds = [calcular_thd(grupos[n][0], len(grupos[n][0])-1, 220, k=0), calcular_thd(grupos[n][1], len(grupos[n][1])-1, 220, k=0), calcular_thd(grupos[n][2], len(grupos[n][2])-1, 220, k=0)]
        for _ in range(len(thds)):
            for i in range(len(thds)-1):
                if thds[i+1] > thds[i]:
                    aux = thds[i]
                    thds[i] = thds[i+1]
                    thds[i+1] = aux
        maiores[n] = thds
    return maiores

def encontrar_grupo(maiores):
    """
    Encontra o grupo em que o THD com maior distorção seja mínimo
    """
    menor = [maiores[0], 0]
    for n in range(len(maiores)):
        if maiores[n][0] < menor[0][0]:
            menor[0] = maiores[n].copy()
            menor[1] = n
        elif maiores[n][0] == menor[0][0]:
            if maiores[n][1] < menor[0][1]:
                menor[0] = maiores[n].copy()
                menor[1] = n
        elif maiores[n][1] == menor[0][1]:
            if maiores[n][2] <= menor[0][2]:
                menor[0] = maiores[n].copy()
                menor[1] = n
    return menor[1]

def saidas2(n_maior, grupos):
    """
    Mostra as saídas da forma que são pedidas
    """
    print("Grupo A")
    if len(grupos[n_maior][0]) == 1:
        print(f"Motor(es): 0")
    else:
        print(f"Motor(es): 0 até {len(grupos[n_maior][0])-1}")
    print(f"THD: {calcular_thd(grupos[n_maior][0], len(grupos[n_maior][0])-1, 220, k=0):.2f} %")
    print()
    print("Grupo B")
    if len(grupos[n_maior][1]) == 1:
        print(f"Motor(es): {len(grupos[n_maior][0])}")
    else:
        print(f"Motor(es): {len(grupos[n_maior][0])} até {len(grupos[n_maior][0])+len(grupos[n_maior][1])-1}")
    print(f"THD: {calcular_thd(grupos[n_maior][1], len(grupos[n_maior][1])-1, 220, k=0):.2f} %")
    print()
    print("Grupo C")
    if len(grupos[n_maior][2]) == 1:
        print(f"Motor(es): {len(grupos[n_maior][0])+len(grupos[n_maior][1])}")
    else:
        print(f"Motor(es): {len(grupos[n_maior][0])+len(grupos[n_maior][1])+len(grupos[n_maior][2]-1)}")
    print(f"THD: {calcular_thd(grupos[n_maior][2], len(grupos[n_maior][2])-1, 220, k=0):.2f} %")