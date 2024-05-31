def raiz(numero):
    """
    Calcula a raiz quadrada de um número
    """
    x_1 = numero/2
    for _ in range(20):
        raiz = (quadrado(x_1) + numero)/ (2*x_1)
        x_1 = raiz

    return raiz

def quadrado(numero):
    """
    Eleva o número dado ao quadrado
    """
    numero = numero*numero

    return numero

def janela(lista, indice_inicial, tamanho_janela):
    """
    Recebe uma string, um índice inicial e o tamanho da janela.
    Devolve uma string correspondente à janela da sequência começando
    no índice inicial fornecido.
    """
    janela = []
    for i in range(indice_inicial, indice_inicial+tamanho_janela):
        janela.append(lista[i])

    return janela

def separar_janelas(lista, tamanho_janela):
    """
    Recebe uma lista e um tamanho de janela e devolve a lista dada dividida em janelas.

    Exemplo: separar_janelas([1,2,3,4,5,6], 2) retorna [[1, 2], [3, 4], [5, 6]]
    """
    i = 0
    lista_janelas= []
    while i != len(lista):
        lista_janelas.append(janela(lista, i, tamanho_janela))
        i += tamanho_janela

    return lista_janelas

def ler_arquivo():
    """
    Recebe uma string com o nome do arquivo.csv e devolve uma lista como os dados do arquivo
    """
    nome_arquivo = input()
    dados = []
    with open(nome_arquivo, newline="\n") as arquivo:
        for linha in arquivo:
            data, temperatura = linha.split(",")
            mes_ano = data.split("/")
            dados.append([(mes_ano[0]),(mes_ano[1]), float(temperatura)])

    return dados

def ordenar_dados(dados):
    """
    Recebe uma lista e ordena os dados contidos nela para em ordem crescente
    """

    n = len(dados)
    for _ in range(n-1):
        for i in range(n-1):
            if dados[i][1] >= dados[i+1][1]:
                aux = dados[i]
                dados[i] = dados[i+1]
                dados[i+1] = aux

    for _ in range(n-1):
        for i in range(n-1):
            if dados[i][0] >= dados[i+1][0] and dados[i][1] >= dados[i+1][1]:
                aux = dados[i]
                dados[i] = dados[i+1]
                dados[i+1] = aux
    
    return dados

def media(lista):
    """
    Calcula a média aritmetica dos itens em uma lista
    """
    soma = 0
    for elemento in lista:
        soma += elemento
    media = soma/len(lista)

    return media

def desvio(lista_medidas):
    """
    Calcula o desvio padrão de uma lista de medidas numéricas
    """
    tamanho = len(lista_medidas)
    variancia = 0
    media_lista = media(lista_medidas)
    for i in range(tamanho):
        variancia += quadrado((lista_medidas[i] - media_lista))
    desvio = raiz(variancia/tamanho)

    return desvio

def temp_media(dados):
    """
    Calcula a temperatura média de cada ano da lista dada
    """
    temps_media = []
    for i in range(0, len(dados), 12):
        ano = janela(dados, i, 12)
        temp_ano = []
        for i in range(len(ano)):
            temp_ano.append(ano[i][2])
        media_ano = media(temp_ano)
        temps_media.append(media_ano)
    
    return temps_media
    
def desvio_anual(dados):
    """
    Calcula o desvio padrão das temperaturas de cada ano em uma lista dada
    """
    desvios = []
    for i in range(0, len(dados), 12):
        ano = janela(dados, i, 12)
        temp_ano = []
        for i in range(len(ano)):
            temp_ano.append(ano[i][2])
        desvio_anual = desvio(temp_ano)
        desvios.append(desvio_anual)

    return desvios

def calcular_outliers(lista_base, parametro1, parametro2):
    """
    Calcula os outliers de uma lista base de meses e anos dada com base nas duas listas de parâmetros dados
    e devolve uma nova lista apenas com os outliners
    """
    outliers = []
    k = 0
    for i in range(len(parametro1)):
        ano = janela(lista_base, k, 12)
        for j in range(len(ano)):
            if parametro1[i] - 1.5*parametro2[i] <= ano[j][2] <= parametro1[i] + 1.5*parametro2[i]:
                pass
            else:
                outliers.append(ano[j])
        k += 12

    return outliers

def media_sem_outlier(lista_base, outliers):
    """
    Calcula a média de uma lista_base excluindo todos os seus elementos que também pertencem
    a lista outliners
    """
    medias = []
    for k in range(0, len(lista_base), 12):
        ano = janela(lista_base, k, 12)
        novo_ano = []
        for i in range(len(ano)):
            if ano[i] not in outliers:
                novo_ano.append(ano[i][2])
        media_i = media(novo_ano)
        medias.append(media_i)
    
    return medias

def media_desvio(lista):
    """
    Recebe uma lista com meses, anos e temperaturas e devolve duas listas, uma com a média histórica
    das temperaturas de cada mês e uma com o desvio padrão histórico de cada mês
    """
    medias = []
    desvios = []
    for k in range(12): #12 -> número de meses
        temp_mes = []
        for i in range(k, len(lista), 12):
            temp_mes.append(lista[i][2])
        media_mes = media(temp_mes)
        desvio_mes = desvio(temp_mes)
        medias.append(media_mes)
        desvios.append(desvio_mes)
    
    return medias, desvios

def discrepancia(n, media, desvio):
    """
    Calcula a discrepancia de um número n com base na média e no desvio padrão dados
    """
    temp_media = quadrado(n-media)
    discrepancia = (raiz(temp_media))/desvio

    return discrepancia

def calcular_discrepancias(lista, media, desvio):
    """
    Recebe 3 listas, umas com meses, anos e temperaturas, uma com as médias históricas referentes a cada mês
    e uma com o desvio histórico referente a cada mês, e devolve uma nova lista com o mês, ano e a discrepancia
    de cada mês, calculada com base na média e no desvio padrão
    """
    discrepancias = []
    for i in range(len(lista)):
        k = i%12
        discrep = [lista[i][0], lista[i][1]]
        dis = discrepancia(lista[i][2], media[k], desvio[k])
        discrep.append(dis)
        discrepancias.append(discrep)

    return discrepancias
    
def maiores_discrepancias(discrepancias, n):
    """
    Recebe uma lista com os meses, anos e as discrepancias e devolve uma lista das N maiores discrepancias,
    acompanhada dos meses e anos respectivos
    """
    maiores_discrepancias = []
    for _ in range(n):
        maior = [0,0,0] #
        for i in range(len(discrepancias)):
            if discrepancias[i][2] > maior[2] and discrepancias[i] not in maiores_discrepancias:
                maior = discrepancias[i]
        maiores_discrepancias.append(maior)
    
    return maiores_discrepancias