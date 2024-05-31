def carregar(img):
    """
    Recebe um arquivo PGM e retorna sua altura, largura e uma matriz com todos os seus números
    """
    with open(img) as arquivo:
        arquivo.readline() #P2
        arquivo.readline() #comentário
        n, m = arquivo.readline().strip().split()
        m = int(m) #linhas
        n = int(n) #colunas
        arquivo.readline().strip() #255
        matriz = []
        for _ in range(m):
            linha = arquivo.readline().strip().split()
            for j in range(n):
                linha[j] = int(linha[j])
            matriz.append(linha)

    return m, n, matriz

def binarizar(matriz, limiar):
    """
    Transforma qualquer valor da matriz dada em 0 ou em 255 com base
    no limiar, sendo menor ou igual a ele se torna 0, sendo maior se torna 255
    """
    cont = 0
    m = len(matriz)
    n = len(matriz[0])
    for i in range(m):
        for j in range(n):
            if matriz[i][j] <= limiar:
                matriz[i][j] = 0
            else:
                matriz[i][j] = 255
                cont += 1
    return cont, matriz

def multiplicar(matriz_a, matriz_b):
    """
    Realiza o produto matricial entre as duas matrizes dadas, substitui a primeira matriz por
    esse produto e retorna o número de valores maiores que 0 na matriz
    """
    assert len(matriz_a) == len(matriz_b)
    m = len(matriz_a)
    n = len(matriz_b[0])
    cont = 0
    
    resultado = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            #for k in range(p):
            #    resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
            resultado[i][j] = matriz_a[i][j] * matriz_b[i][j]
    
    for i in range(len(resultado)):
        for j in range(len(resultado[0])):
            #matriz_a[i][j] = resultado[i][j]
            if resultado[i][j] > 0:
                cont += 1
            
    return [cont, resultado]

def somar(matriz_a, matriz_b):
    """
    Soma cada elemento da matriz_a com seu respectivo elemento na matriz_b e
    cada elemento da nova matriz_ab é a média dessa soma
    """
    assert len(matriz_a) == len(matriz_b)
    m = len(matriz_a)
    n = len(matriz_b[0])
    matriz_ab = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(len(matriz_a)):
        for j in range(len(matriz_b[0])):
            matriz_ab[i][j] = (matriz_a[i][j] + matriz_b[i][j])/2
    
    return matriz_ab

def normalizar_valor(valor_inicial, max_inicial, min_inicial):
    """
    Calcula o novo valor normalizado, com base nos antigos máximos e minimos do arquivo PGM
    """
    assert max_inicial != 0
    novo_valor = (255*(valor_inicial - min_inicial))/(max_inicial - min_inicial)

    return int(novo_valor)

def normalizar(matriz):
    """
    Recebe uma matriz numérica e normaliza ela, com o valor máximo sendo 0
    e o mínimo sendo 255, devolvendo o número de entradas maiores que zero da matriz já normalizada 
    """
    cont = 0
    max = matriz[0][0]
    min = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > max:
                max = matriz[i][j]
            elif matriz[i][j] < min:
                min = matriz[i][j]

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            #if matriz[i][j] == max:
                #matriz[i][j] = 255
            #else:
            matriz[i][j] = normalizar_valor(matriz[i][j], max, min)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > 0:
                cont += 1

    return cont


def filtrar(mm, mf):
    """
    Aplica o filtro pedido para cada mini matriz e recebendo a matriz de filtro, devolve o 
    novo pixel equivalente com o filtro aplicado
    """
    novo_pixel = 0
    for i in range(len(mm)):
        for j in range(len(mm[0])):
            novo_pixel += mm[i][j] * mf[i][j]

    return(novo_pixel)

def laplace(matriz):
    """
    Aplica o filtro laplaciano em toda a matriz, devolvendo o número de pixels maiores que zero
    da nova matriz filtrada
    """
    cont = 0
    matriz_filtro = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
    matriz_copia = [[0 for j in range(len(matriz[0]))] for i in range(len(matriz))]
    for i in range(1,len(matriz)-1):
        for j in range(1,len(matriz[0])-1):
                mini_matriz = [[matriz[i-1][j-1],matriz[i-1][j],matriz[i-1][j+1]],[matriz[i][j-1],matriz[i][j],matriz[i][j+1]],[matriz[i+1][j-1],matriz[i+1][j],matriz[i+1][j+1]]]
                matriz_copia[i][j] = filtrar(mini_matriz,matriz_filtro)
                if matriz_copia[i][j] > 0:
                    cont += 1 
                    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = matriz_copia[i][j]

    return cont
    
def gravar(nome, matriz,):
    """
    Recebe o nome do arquivo que deseja ser criado, a matriz que 
    ira gerar esse arquivo e sua largura e altura, respectivamente
    """
    with open(nome, "w") as arquivo:
        arquivo.write("P2")
        arquivo.write("\n")
        arquivo.write(f"# {nome}")
        arquivo.write("\n")
        n = str(len(matriz[0]))
        m = str(len(matriz))
        arquivo.write(n)
        arquivo.write(" ")
        arquivo.write(m)
        arquivo.write("\n255\n")
        for i in range(int(m)):
            if "\n" not in matriz[i]:
                matriz[i].append("\n")
            for j in range(len(matriz[0])):
                if matriz[i][j] != "\n":
                    matriz[i][j] = int(matriz[i][j])
                    matriz[i][j] = str(matriz[i][j]) + " "
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                arquivo.write(matriz[i][j])

def ler_entradas():
    """
    Recebe entradas do teclado e as amazena em um vetor e devolve-o quando detecta o erro EOFError
    """
    entradas = []
    try:
        while True:
            entrada = input().split()
            entradas.append(entrada)

    except EOFError:
        return entradas

