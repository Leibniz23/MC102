def ler_entradas():
    """
    Recebe entradas do terminal e, ao receber a entrada "terminar" retorna uma
    lista com as entradas coletadas, incluindo "terminar"
    """
    entradas = []
    while True:
        entrada = input().split()
        entradas.append(entrada)
        if entrada[0] == "terminar":
            return entradas

def arquivo(nome, conteudo, usuario):
    """
    Cria uma lista com o nome fornecido, uma lista vazia, o usuário ativo no momento e a data de criação
    do arquivo e retorna essa lista e o status dessa lista antes da execução da função, caso a lista já
    existisse, retorna False, caso tenha sido criada no momento, retorna True
    """
    arquivo = [nome, conteudo, usuario]

    return arquivo

def ler_arquivo(arquivo):
    """
    Lê um arquivo linha a linha e transforma cada palavra em um item da matriz
    """
    with open(arquivo) as arquivo:
        matriz = []
        while True:
            linha = arquivo.readline().split(" ")
            if linha == ['']:
                return matriz
            matriz.append(linha)


def alfabetica(palavra_a, palavra_b):
    """
    Verifica se a palavra_a vem antes da palavra_b na ordem alfabética, se isso ocorrer ela retorna
    True, se for o contrário retorna False
    """
    resp = False
    for i in range(len(palavra_b)):
        if i < len(palavra_a):
            if palavra_a[i] != palavra_b[i]:
                if palavra_a[i] < palavra_b[i] :
                    resp = True
                else:
                    resp = False
                return resp
        else:
            resp = True
    return resp

def ord_lista(lista):
    """
    Organiza uma lista em ordem alfabetica, tomando como base o primeiro item de cada um de seus elementos
    """
    arq_ord = []
    n = len(lista)
    disp = list(range(n))
    while len(disp) > 0:
        menor = disp[0]
        for i in range(len(disp)):
            if alfabetica(lista[disp[i]][0], lista[menor][0]):
                menor = disp[i]
        arq_ord.append(menor)
        disp.pop(disp.index(menor))

    return arq_ord

def comparar(arquivo1, arquivo2):
    """
    Retorna as linhas que contém diferenças nas duas listas
    """
    linhas_1 = []
    linhas_2 = []
    for i in range(len(arquivo1)):
        if arquivo1[i] != arquivo2[i]:
            linhas_1.append(arquivo1[i])
            linhas_2.append(arquivo2[i])

    return linhas_1, linhas_2

def unix(diff):
    """
    Recebe uma tupla com duas listas, e mostra as duas na tela nas configurações de 
    diff do Unix
    """
    n = len(diff[0])
    for i in range(n):
        print("<",*diff[0][i],sep=" ",end="")
    print("---")
    for i in range(n):
        print(">",*diff[1][i],sep=" ",end="")

def ord_nomes(corresp, nome):
    """
    Modifica a lista dada e a coloca em ordem alfabética
    """
    n = len(corresp)
    if(n>0):
        if(alfabetica(corresp[n-1],nome)):
            corresp.append(nome)
        else:        
            for i in range(n):
                if alfabetica(nome, corresp[i]):
                    corresp.insert(i, nome)
                    break
    else:
        corresp.append(nome)

def in_arq(arq,text):
    """
    Retorna True se text está na lista e False caso contrário
    """
    novo_arq = set()
    for i in range(len(arq)):
        for j in range(len(arq[i])):
            novo_arq.add(arq[i][j])
    #print(novo_arq)

    if text in novo_arq:
        return True

    elif text+"\n" in novo_arq:
        return True
    return False