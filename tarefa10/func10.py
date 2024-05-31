def fatorial(n):
    """Calcula o fatorial de um número n dado"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

def stifel(n, k):
    """
    Calcula o binômio de Newton através da relação de Stifel
    """
    if n == k or n == 0:
        return 1
    elif k == 0:
        return 1
    elif k == 1:
        return n
    else:
        return stifel(n-1, k-1) + stifel(n-1, k)

def mdc(a, b):
    """Calcula o MDC entre a e b"""
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        if a >= b:
            return mdc(a-b, b)
        elif b > a:
            return mdc(b-a, a)

def fibonacci(n, sequencia = {1:1, 2:1, 3:1}):
    """
    Calcula o valor do n-ésimo termo da sequência de Fibonacci com saltos
    """
    try:
        return sequencia[n]
    except KeyError:
        fn = fibonacci(n-1) + fibonacci(n-3)
        sequencia[n] = fn
        return sequencia[n]

def busca(i, lista, lim_min, lim_max):
    """Retorna a posição do elemento i na lista dada"""
    if lim_min < lim_max:
        return
    else:
        m = (lim_max + lim_min) // 2
        if i == lista[m]:
            return m
        elif lista[m] < i:
            return busca(i, lista, m-1, lim_max)
        elif lista[m] > i:
            return busca(i, lista, lim_min, m+1)
        

def contar(i, lista):
    """
    Conta quantas vezes o elemento i aparece na lista dada
    """
    alvo = busca(i, lista, len(lista)-1, 0)
    if alvo == None:
        return 0
    else:
        copia = lista.copy()
        copia.pop(alvo)
        return 1 + contar(i, copia)

def soma(lista, i=0):
    """
    Soma todos os valores de uma lista usando recursão
    """
    if i < len(lista):
        return lista[i] + soma(lista, i+1)
    else:
        return 0

def prob(n, x, probis={}):
    """
    Calcula a probabilidade de João receber a recompensa de Maria
    """
    if x == 0:
        return 1
    elif x < 0:
        return 0
    elif n == 0:
        return 0
    else:
        if (n, x) in probis:
            return probis[(n, x)]
        else:
            probs = soma([prob(n-1, x-6), prob(n-1, x-5), prob(n-1, x-4), prob(n-1, x-3), prob(n-1, x-2), prob(n-1, x-1)])*1/6
            probis[(n, x)] = probs
            return probis[(n, x)]




